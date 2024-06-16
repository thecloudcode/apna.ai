import requests
import spacy
nlp = spacy.load("en_core_web_sm")

# rating = "7.7"

def score(string1, string2):
    string1_nlp = nlp(string1)
    string2_nlp = nlp(string2)

    similarity_score = string1_nlp.similarity(string2_nlp)
    return similarity_score

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


def result(resume_parsed):
    job = getjob_details()
    resume_score = 0
    for i in job:
        resume_score += score(resume_parsed, i['Description'])*10
    rating = resume_score/len(getjob_details())
    ranks = getranks(rating)
    ranks_list = []
    for i, j in ranks.items():
        ranks_list.append(j)
    ind = 0
    for i in job:
        i['Rank'] = ranks_list[ind]
        i['Description'] = None
        ind+=1

    res = job
    return job

# x = result(" Nitin Das  +91 7428774640 # nitin23329@gmail.com ï linkedin.com/in/nitin-das Education IIIT Delhi, India July 2019 – May 2023 Bachelor of Technology In Electronics and Communication CGPA: 8.32/10 Relevant Coursework • Data Structures and Algorithms • Competitive Programming • Computer Networks • Operating System • Database Management System • Object Oriented Programming • Machine Learning • Distributed Systems • Cloud Computing Experience Walmart July 2023 – Present Software Engineer II Bangalore, Karnataka • Migration of Jupyter Notebook service from CentOS-based k8s Containers to Ubuntu-based Containers • Developed and tested Springboot backend GET, PATCH, DELETE APIs which is connected to SQL Database. Expedia May 2022 – July 2022 Software Engineer Intern Gurugram, Haryana • Developed an e2e NLU service for a chatbot. Leveraged Python scripting and NLP techniques to populate and preprocess user utterances for model training. Achieved an impressive 95% classification accuracy using ML model. Deployed the service on AWS EC2 with Flask • Developed loading animations for improved user experience during page load, integrated UI alert animations for real-time feedback on backend API failures, and configured the UI for three distinct user roles, enhancing usability and functionality using ReactJS FreshPrints Jan 2023 – April 2023 Full Stack Web Intern Remote, Bangalore • Devleloped NodeJS backend service to fetch and parse invoice data from the MySQL database using Sequelize. • Wrote Dockerfile script to create a docker image for the service. • Created a CI/CD automation pipeline using CirceCi to push Docker Image to AWS ECR. Projects Crop Recommendation Model | Machine Learning, Exploratory Data Analysis, Model Tuning, Evaluation and Comparision • This Machine Learning project aims to find the best suitable crop for given agricultural land by analyzing various climatic conditions and soil features. Several ML algorithms have been analyzed and compared. • Models compared: Logistic Regression, Naive Bayes, Decision Tree, Random Forest, Artificial Neural Network. Online Retail System | ER-Diagram, MySQL, Relational schemas, indexing, grants, triggers • Created a clone of an Online Retail system like Amazon using DBMS concepts. • For frontend, A JFrame GUI was created, and a connection was made to our MYSQL database. Technical Skills Languages: Java, Python, C++, JavaScript, SQL. Technologies/Frameworks: Docker, Kubernetes, Springboot, ReactJS, NodeJS, Flask, Machine learning, Natural language processing, AWS, CI/CD, MySQL, Git and GitHub. Algorithmic Competitions Achivements • Expert at Codeforces (1703) • 5-start Java coder at Hackerrank • solved 3000+ problems across various Programming sites • Global rank 99/5k+ in Codechef round #LTIME94C • Global Rank 1216/12k in Google Kickstart 2022 • India rank of 549 out of 5k+ participants in ICPC Preliminary Round 2021 Position of Responsibility • FooBar, Competitive Programming Club of IIIT Delhi • TA of Competitive Programming (CSE 200) • TA of Object Oriented Programming (CSE 201)")
# for i in x:
#     print(i['Rank'], i)
# def result(rating):
#     score =  getranks(rating)
#     job = getjob_details()
#
#     ranks = []
#     for i,j in score.items():
#         ranks.append(j)
#     ind = 0
#     for i in job:
#         i['Rank'] = ranks[ind]
#         i['Description'] = None
#         ind+=1
#
#     res = job
#     return job
