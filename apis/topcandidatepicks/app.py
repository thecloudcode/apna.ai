from fastapi import FastAPI, HTTPException
from typing import List
import os
import requests

app = FastAPI()

@app.get("/getcandidates")
def get_applicants(id: str, numofcandidates: int):
    url = "https://db-crud-fastapi.onrender.com/get_data_from_applicants_rating_data"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status
        data = response.json()

        data2 = []
        for i in data:
            data2.append([i['Id'], int(i[str(id)])])
        sorted_data2 = sorted(data2, key=lambda x: x[1])[:numofcandidates]
        ids = [i[0] for i in sorted_data2]

        url2 = "https://apna-ai-wsfp.onrender.com/getusers"
        response = requests.get(url2)
        response.raise_for_status()
        users = response.json()

        res = [i for i in users if i['user_id'] in ids]
        return res

    except requests.exceptions.HTTPError as http_err:
        raise HTTPException(status_code=response.status_code, detail=str(http_err))
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))

if __name__ == "__main__":
    import uvicorn
    # port = int(os.environ.get('PORT', 8000))
    uvicorn.run(app, host='0.0.0.0', port=8000)