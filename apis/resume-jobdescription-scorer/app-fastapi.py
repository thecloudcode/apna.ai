import os
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import spacy
from dotenv import load_dotenv
import logging

load_dotenv()
logging.basicConfig(level=logging.INFO)

nlp = spacy.load("en_core_web_sm")

app = FastAPI()

# Define Pydantic models for request bodies
class SimilarityRequest(BaseModel):
    string1: str
    string2: str

@app.post("/similarity")
async def similarity(request: SimilarityRequest):
    """
    Endpoint to compute similarity score between two strings.

    Expected JSON Format:
    {
        "string1": "First string for comparison",
        "string2": "Second string for comparison"
    }
    """
    string1 = request.string1
    string2 = request.string2

    try:
        w1 = nlp(string1)
        w2 = nlp(string2)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error processing input strings")

    try:
        similarity_score = w1.similarity(w2)
    except Exception as e:
        raise HTTPException(status_code=500, detail="Error computing similarity score")

    return {"similarity": similarity_score}

if __name__ == '__main__':
    import uvicorn
    port = int(os.environ.get('PORT', 8000))
    uvicorn.run(app, host='0.0.0.0', port=port)
