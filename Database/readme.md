# 🌐 apna.ai Database Architecture

Welcome! This README provides an overview of the database architecture, including the tables, their relationships, and an illustration of the schema.

![Screenshot 2024-06-16 194616](https://github.com/thecloudcode/apna.ai/assets/114615639/39650015-8778-4efb-906a-49e0f8a83c47)

## 🗂️ Tables Overview

### 👥 Users

| Column       | Type         | Constraints                                            |
|--------------|--------------|--------------------------------------------------------|
| User_id      | SERIAL       | PRIMARY KEY                                            |
| Name         | VARCHAR(100) | NOT NULL                                               |
| Email        | VARCHAR(100) | UNIQUE, NOT NULL                                       |
| Phone_Number | VARCHAR(15)  |                                                        |
| User_Type    | VARCHAR(50)  | NOT NULL, CHECK (User_Type IN ('Employer', 'Jobseeker'))|

The `Users` table stores basic information about all users of the website, including employers and job seekers.

### 🏢 Employers

| Column        | Type         | Constraints                           |
|---------------|--------------|---------------------------------------|
| Employer_id   | SERIAL       | PRIMARY KEY                           |
| User_id       | INT          | NOT NULL, FOREIGN KEY REFERENCES Users(User_id) ON DELETE CASCADE |
| Company_Name  | VARCHAR(100) | NOT NULL                              |

The `Employers` table extends the `Users` table for users who are employers, storing additional details such as the company name.

### 📄 Jobseekers

| Column         | Type         | Constraints                           |
|----------------|--------------|---------------------------------------|
| Jobseeker_id   | SERIAL       | PRIMARY KEY                           |
| User_id        | INT          | NOT NULL, FOREIGN KEY REFERENCES Users(User_id) ON DELETE CASCADE |
| Resume         | TEXT         |                                       |

The `Jobseekers` table extends the `Users` table for users who are job seekers, storing additional details such as the resume.

### 📝 Applications

| Column          | Type         | Constraints                           |
|-----------------|--------------|---------------------------------------|
| Application_id  | SERIAL       | PRIMARY KEY                           |
| Jobseeker_id    | INT          | NOT NULL, FOREIGN KEY REFERENCES Jobseekers(Jobseeker_id) ON DELETE CASCADE |
| Job_id          | INT          | NOT NULL, FOREIGN KEY REFERENCES Current_Job_Openings(Job_id) ON DELETE CASCADE |
| Date_Applied    | DATE         | NOT NULL                              |
| Status          | VARCHAR(50)  | NOT NULL                              |

The `Applications` table records job applications made by job seekers.

### 📌 Current Job Openings

| Column        | Type         | Constraints                            |
|---------------|--------------|----------------------------------------|
| Job_id        | SERIAL       | PRIMARY KEY                            |
| Company       | VARCHAR(100) | NOT NULL                               |
| Role          | VARCHAR(100) | NOT NULL                               |
| Description   | TEXT         |                                        |
| Salary        | DECIMAL(10,2)|                                        |
| Location      | VARCHAR(100) |                                        |
| Mode          | VARCHAR(50)  | CHECK (Mode IN ('Onsite', 'Remote', 'Hybrid')) |

The `Current_Job_Openings` table stores details about available job positions.

### 📊 Fact Table

| Column          | Type         | Constraints                           |
|-----------------|--------------|---------------------------------------|
| Fact_id         | SERIAL       | PRIMARY KEY                           |
| User_id         | INT          | NOT NULL, FOREIGN KEY REFERENCES Users(User_id) ON DELETE CASCADE |
| Job_id          | INT          | NOT NULL, FOREIGN KEY REFERENCES Current_Job_Openings(Job_id) ON DELETE CASCADE |
| Application_id  | INT          | NOT NULL, FOREIGN KEY REFERENCES Applications(Application_id) ON DELETE CASCADE |

The `Fact_Table` is used for analytical purposes, connecting users, job openings, and applications.

### ⭐ Applicants Rating Data

| Column  | Type  | Constraints |
|---------|-------|-------------|
| Id      | SERIAL| PRIMARY KEY |
| 101     | FLOAT |             |
| 102     | FLOAT |             |
| 103     | FLOAT |             |
| 104     | FLOAT |             |
| 105     | FLOAT |             |
| 106     | FLOAT |             |
| 107     | FLOAT |             |
| 108     | FLOAT |             |
| 109     | FLOAT |             |
| 110     | FLOAT |             |
| 111     | FLOAT |             |
| 112     | FLOAT |             |
| 113     | FLOAT |             |
| 114     | FLOAT |             |
| 115     | FLOAT |             |
| 116     | FLOAT |             |
| 117     | FLOAT |             |

The `Applicants_Rating_Data` table stores rating data for applicants across various criteria.

## 🏗️ Database Architecture

```mermaid
erDiagram
    USERS {
        SERIAL User_id PK
        VARCHAR(100) Name
        VARCHAR(100) Email UNIQUE
        VARCHAR(15) Phone_Number
        VARCHAR(50) User_Type
    }
    EMPLOYERS {
        SERIAL Employer_id PK
        INT User_id FK
        VARCHAR(100) Company_Name
    }
    JOBSEEKERS {
        SERIAL Jobseeker_id PK
        INT User_id FK
        TEXT Resume
    }
    APPLICATIONS {
        SERIAL Application_id PK
        INT Jobseeker_id FK
        INT Job_id FK
        DATE Date_Applied
        VARCHAR(50) Status
    }
    CURRENT_JOB_OPENINGS {
        SERIAL Job_id PK
        VARCHAR(100) Company
        VARCHAR(100) Role
        TEXT Description
        DECIMAL(10, 2) Salary
        VARCHAR(100) Location
        VARCHAR(50) Mode
    }
    FACT_TABLE {
        SERIAL Fact_id PK
        INT User_id FK
        INT Job_id FK
        INT Application_id FK
    }
    APPLICANTS_RATING_DATA {
        SERIAL Id PK
        FLOAT "101"
        FLOAT "102"
        FLOAT "103"
        FLOAT "104"
        FLOAT "105"
        FLOAT "106"
        FLOAT "107"
        FLOAT "108"
        FLOAT "109"
        FLOAT "110"
        FLOAT "111"
        FLOAT "112"
        FLOAT "113"
        FLOAT "114"
        FLOAT "115"
        FLOAT "116"
        FLOAT "117"
    }

    USERS ||--o{ EMPLOYERS : has
    USERS ||--o{ JOBSEEKERS : has
    USERS ||--o{ FACT_TABLE : records
    EMPLOYERS ||--o{ CURRENT_JOB_OPENINGS : posts
    JOBSEEKERS ||--o{ APPLICATIONS : applies
    CURRENT_JOB_OPENINGS ||--o{ APPLICATIONS : receives
    CURRENT_JOB_OPENINGS ||--o{ FACT_TABLE : records
    APPLICATIONS ||--o{ FACT_TABLE : contains
    JOBSEEKERS ||--o{ FACT_TABLE : recorded_in
