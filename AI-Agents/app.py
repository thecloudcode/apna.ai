"""
Model : flan-t5-base
This is not the model used in Agent right now, for a future task
"""

import os
from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel
from langchain import HuggingFaceHub
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferMemory
from crew import result
from fastapi.middleware.cors import CORSMiddleware


load_dotenv()
HUGGING_FACE_HUB_API_KEY = os.getenv("HUGGINGFACEHUB_API_TOKEN")

repo_id = 'google/flan-t5-base'
llm = HuggingFaceHub(
    huggingfacehub_api_token=HUGGING_FACE_HUB_API_KEY,
    repo_id=repo_id,
    model_kwargs={'temperature': 1.0, 'max_length': 32}
)

memory = ConversationBufferMemory()
conversation_buf = ConversationChain(
    llm=llm,
    memory=memory
)

repo_id2 = 'databricks/dolly-v2-3b'
llm2 = HuggingFaceHub(
    huggingfacehub_api_token=HUGGING_FACE_HUB_API_KEY,
    repo_id=repo_id2,
    model_kwargs={'temperature': 1.0, 'max_length': 32}
)

memory2 = ConversationBufferMemory()
conversation_buf2 = ConversationChain(
    llm=llm2,
    memory=memory2
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins, change this to specific domains in production
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

class QueryRequest(BaseModel):
    query: str

@app.post("/predict")
async def predict(query_request: QueryRequest):
    query = query_request.query
    prediction1 = conversation_buf.predict(input=query)
    prediction2 = conversation_buf2.predict(input=query)
    return {"prediction1": prediction1, "prediction2": prediction2}

@app.post("/agents")
async def agents(query_request: QueryRequest):
    query = query_request.query
    res = result(query)
    return res

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
