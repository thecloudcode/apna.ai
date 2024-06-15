from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from google.generativeai import configure, GenerativeModel
from dotenv import load_dotenv
import uvicorn

load_dotenv()

configure(api_key=os.getenv("GOOGLE_API_KEY"))
generation_config = {"temperature": 0.9, "top_p": 1, "top_k": 1, "max_output_tokens": 2048}

app = FastAPI()
model = GenerativeModel("gemini-pro", generation_config=generation_config)

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
async def generate_response(request: PromptRequest):
    if not request.prompt:
        raise HTTPException(status_code=400, detail="No prompt provided")

    response = model.generate_content([request.prompt])
    return {"response": response.text}

if __name__ == "__main__":
    port = int(os.getenv('PORT', 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
