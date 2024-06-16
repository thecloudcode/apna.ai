import requests

# rating = "7.7"

def getranks(rating):
    url = "https://resume-scorer-fastapi.onrender.com/rank"
    payload = {
        "score" : rating
    }
    headers = {
        "Content-Type" : "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return {
            "error" : f"Request failed {response.status_code}",
            "details" : response.text
        }

def getjob_details():
    url = "https://db-crud-fastapi.onrender.com/get_data_from_current_job_openings"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return {
            "error": f"Request failed {response.status_code}",
            "details": response.text
        }

def result(rating):
    score =  getranks(rating)
    job = getjob_details()

    ranks = []
    for i,j in score.items():
        ranks.append(j)
    ind = 0
    for i in job:
        i['Rank'] = ranks[ind]
        i['Description'] = None
        ind+=1

    res = job
    return job
