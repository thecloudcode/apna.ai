import os
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from score import score_resume, extract_text_from_pdf
from rankings import result

app = FastAPI()

# Set up static file serving for the uploads folder
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

# Allowed file extensions
ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
        <head>
            <title>Resume Upload</title>
        </head>
        <body>
            <h1>Upload your resume</h1>
            <form action="/upload" method="post" enctype="multipart/form-data">
                <input type="file" name="resume">
                <input type="submit" value="Upload">
            </form>
        </body>
    </html>
    """

@app.post("/upload")
async def upload_file(resume: UploadFile = File(...)):
    if resume.filename == '':
        raise HTTPException(status_code=400, detail="No file uploaded")

    if not allowed_file(resume.filename):
        raise HTTPException(status_code=400, detail="Invalid file type")

    file_location = os.path.join('uploads', resume.filename)
    with open(file_location, "wb+") as file_object:
        file_object.write(resume.file.read())

    try:
        score = result(file_location)
        # score = score_resume(file_location)  # Uncomment this line if using score_resume function
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error processing resume")

    return {"score": score}

if __name__ == '__main__':
    import uvicorn
    port = int(os.environ.get('PORT', 8000))
    uvicorn.run(app, host='0.0.0.0', port=port)
