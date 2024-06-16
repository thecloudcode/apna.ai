import requests

rating = "7.7"

def getranks(score):
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

result = getranks("7.7")
print(result)