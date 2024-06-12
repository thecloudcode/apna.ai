from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from supabase import create_client, Client
import os
from dotenv import load_dotenv
import logging
from fastapi.middleware.cors import CORSMiddleware

load_dotenv()

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins, change this to specific domains in production
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)
logging.basicConfig(level=logging.INFO)

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# Define Pydantic models for request bodies
class ApplicantsRatingData(BaseModel):
    Id: int
    Name: str

class CurrentJobOpenings(BaseModel):
    Job_id: int
    Company: str = None

@app.post("/add_data_to_applicants_rating_data")
async def add_data_to_applicants_rating_data(data: ApplicantsRatingData):
    try:
        response = supabase.table('Applicants_Rating_Data').insert(data.dict()).execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/delete_data_from_applicants_rating_data/{id}")
async def delete_data_from_applicants_rating_data(id: int):
    try:
        response = supabase.table('Applicants_Rating_Data').delete().eq('Id', id).execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/update_data_from_applicants_rating_data/{id}")
async def update_data_from_applicants_rating_data(id: int, data: ApplicantsRatingData):
    try:
        response = supabase.table('Applicants_Rating_Data').update(data.dict()).eq('Id', id).execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/get_data_from_applicants_rating_data")
async def get_data_from_applicants_rating_data():
    try:
        response = supabase.table('Applicants_Rating_Data').select('*').execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/add_data_to_current_job_openings")
async def add_data_to_current_job_openings(data: CurrentJobOpenings):
    try:
        response = supabase.table('Current_Job_Openings').insert(data.dict()).execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.delete("/delete_data_from_current_job_openings/{id}")
async def delete_data_from_current_job_openings(id: int):
    try:
        response = supabase.table('Current_Job_Openings').delete().eq('Job_id', id).execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.put("/update_data_from_current_job_openings/{id}")
async def update_data_from_current_job_openings(id: int, data: CurrentJobOpenings):
    try:
        response = supabase.table('Current_Job_Openings').update(data.dict()).eq('Job_id', id).execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/get_data_from_current_job_openings")
async def get_data_from_current_job_openings():
    try:
        response = supabase.table('Current_Job_Openings').select('*').execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

if __name__ == '__main__':
    import uvicorn
    port = int(os.environ.get('PORT', 8000))
    uvicorn.run(app, host='0.0.0.0', port=port)
