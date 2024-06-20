import requests

def get_applicants(id: str, numofcandidates: int):
    url = "https://db-crud-fastapi.onrender.com/get_data_from_applicants_rating_data"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status
        data = response.json()
        # print(data)
        data2 = []
        for i in data:
            data2.append([i['Id'], int(i[str(id)])])
        sorted_data2 = sorted(data2, key=lambda x: x[1])[::-1][:numofcandidates]
        ids = [i[0] for i in sorted_data2]
        # print(sorted_data2)
        url2 = "https://apna-ai-wsfp.onrender.com/getusers"
        response = requests.get(url2)
        response.raise_for_status()
        users = response.json()
        res = []
        res = [i for i in users if i['user_id'] in ids]

        for i in res:
            # i['Score'] = data[0][str(i['user_id']]
            for j in data:
                if j['Id'] == i['user_id']:
                    i['Score'] = j[str(id)]
        return res

    except Exception as e:
        return e

print(get_applicants(103,5))