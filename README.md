# Apna.ai

Welcome to the Apna.ai project! This repository contains multiple APIs designed to streamline various tasks such as resume scoring, job description matching, and database CRUD operations. Below are the details of the available APIs.

## 🏗️ Database Architecture

```mermaid
erDiagram
    USERS ||--o{ EMPLOYERS : has
    USERS ||--o{ JOBSEEKERS : has
    USERS ||--o{ FACT_TABLE : records
    EMPLOYERS ||--o{ CURRENT_JOB_OPENINGS : posts
    JOBSEEKERS ||--o{ APPLICATIONS : applies
    CURRENT_JOB_OPENINGS ||--o{ APPLICATIONS : receives
    CURRENT_JOB_OPENINGS ||--o{ FACT_TABLE : records
    APPLICATIONS ||--o{ FACT_TABLE : contains
    JOBSEEKERS ||--o{ FACT_TABLE : recorded_in
    APPLICANTS_RATING_DATA
```

# 🌐 APIs

### ✨ Custom Gemini Response

**Base URL:** [https://gogemini.onrender.com](https://gogemini.onrender.com)
- **Endpoint:** `/generate`
- **HTTP Method:** `POST`
```json
{
    "prompt": "I am Badal"
}
```

### 📈 Resume Rank Calculator

**Base URL:** [https://resume-scorer-fastapi.onrender.com](https://resume-scorer-fastapi.onrender.com)
- **Endpoint:** `/rank`
- **HTTP Method:** `POST`
```json
{
    "score": "7.7"
}
```

### 📝 Resume - Job Description Scorer

**Base URL:** [https://resume-jobdes-scorer.onrender.com](https://resume-scorer-fastapi.onrender.com)
- **Endpoint:** `/similarity`
- **HTTP Method:** `POST`
```json
{
    "string1": "Help me out",
    "string2": "Please, help me out"
}
```

### ⚡ Quick Actions on Applicants Rating Data

**Base URL:** [https://db-crud-fastapi.onrender.com](https://db-crud-fastapi.onrender.com)
- **Endpoint:** `/add_data_to_applicants_rating_data`
- **HTTP Method:** `POST`
```json
{
    "Id": "103"
    // other attributes are ignored for simplicity example
}
```
- **Endpoint:** `/delete_data_from_applicants_rating_data`
- **HTTP Method:** `DELETE`


- **Endpoint:** `update_data_from_applicants_rating_data/<int:Id>`
- **HTTP Method:** `PUT`
```json
{
    "103": 7.7
    // other attributes are ignored for simplicity example
}
```
- **Endpoint:** `/get_data_from_applicants_rating_data`
- **HTTP Method:** `GET`

### 🚀 Quick Actions on Current Job Openings Data

- **Endpoint:** `add_data_to_current_job_openings`
- **HTTP Method:** `POST`
```json
{
    "Job_id": "118"
    // other attributes are ignored for simplicity example
}
```
- **Endpoint:** `/delete_data_from_current_job_openings/<int:id>`
- **HTTP Method:** `DELETE`


- **Endpoint:** `/update_data_from_current_job_openings/<int:id>`
- **HTTP Method:** `POST`
```json
{
    "Name": "Jane Doe"
    // other attributes are ignored for simplicity example
}
```


- **Endpoint:** `/get_data_from_current_job_openings`
- **HTTP Method:** `GET`
