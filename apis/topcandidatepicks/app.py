import requests

def get_appslicants(id, numofcandidates):
    url = "https://db-crud-fastapi.onrender.com/get_data_from_applicants_rating_data"
    try:
        response = requests.get(url)
        data = response.json()

        print(data)
        data2 = {}
        for i in data:
            if(i['Id'] == id):
                data2 = i
        del data2['Name']
        del data2['Id']
        sorted_data2 = dict(sorted(data2.items(), key=lambda item: item[1], reverse=True)[:numofcandidates])
        print(sorted_data2)

        url2 = "https://apna-ai-wsfp.onrender.com/getusers"
        response = requests.get(url2)
        users = response.json()
        
        res = {}


    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")


get_appslicants(1002, 10)