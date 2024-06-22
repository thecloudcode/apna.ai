from flask import Flask, request, jsonify, render_template # type: ignore
from flask_mysqldb import MySQL # type: ignore

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Yashsai07@'
app.config['MYSQL_DB'] = 'API'

mysql = MySQL(app)

@app.route('/')
def home():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    data = cur.fetchall()
    cur.close()
    return render_template('index.html', data=data)

# API to create a new user
@app.route('/api/users', methods=['POST'])
def create_user():
    name = request.json['name']
    email = request.json['email']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'User created successfully'}), 201

# API to get all users
@app.route('/api/users', methods=['GET'])
def get_users():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    cur.close()
    return jsonify(users)

# API to get a user by ID
@app.route('/api/users/<int:id>', methods=['GET'])
def get_user(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM users WHERE id = %s", (id,))
    user = cur.fetchone()
    cur.close()
    if user:
        return jsonify(user)
    return jsonify({'message': 'User not found'}), 404

# API to update a user by ID
@app.route('/api/users/<int:id>', methods=['PUT'])
def update_user(id):
    name = request.json['name']
    email = request.json['email']
    cur = mysql.connection.cursor()
    cur.execute("UPDATE users SET name = %s, email = %s WHERE id = %s", (name, email, id))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'User updated successfully'})

# API to delete a user by ID
@app.route('/api/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM users WHERE id = %s", (id,))
    mysql.connection.commit()
    cur.close()
    return jsonify({'message': 'User deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
