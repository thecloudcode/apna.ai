from flask import Flask, request, jsonify, abort
from flask_mail import Mail, Message
import logging
from logging.handlers import RotatingFileHandler

app = Flask(__name__)

# Email configuration
gmailID = "apanplacement1@gmail.com"
gPass = "Apna1@place"

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = gmailID
app.config['MAIL_PASSWORD'] = gPass
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

# Set up logging
handler = RotatingFileHandler('error.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.DEBUG)
app.logger.addHandler(handler)

@app.errorhandler(400)
def not_data(error):
    response = jsonify({"Error": error.description })
    response.status_code = 400
    return response

@app.errorhandler(500)
def internal_error(error):
    response = jsonify({"Error": "Internal Server Error"})
    response.status_code = 500
    app.logger.error(f"Server Error: {error}, route: {request.url}", exc_info=True)
    return response

@app.route("/mail", methods=['POST'])
def sendMailWithCustomBody():
    try:
        reqBody = request.get_json()
        if not reqBody:
            abort(400, "Body Is Missed")

        subject = reqBody.get("subject", "Hello")
        recipient = reqBody.get("toMailId")
        if recipient is None:
            abort(400, "toMailId Is Missed in Body")

        msg = Message(
            subject,
            sender=gmailID,
            recipients=[recipient]
        )
        msg.body = reqBody.get("mailBody", 'Hello Flask message sent from Flask-Mail')
        mail.send(msg)

        response = {"Status": "Message Sent"}
        return jsonify(response), 201

    except Exception as e:
        app.logger.error(f"Error sending email: {e}", exc_info=True)  # Log the exception with traceback
        abort(500)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
