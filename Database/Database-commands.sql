-- Create table: Activity_Scorer
CREATE TABLE Activity_Scorer (
    user_id SERIAL PRIMARY KEY,
    chatbot_interactions INTEGER,
    website_visits INTEGER,
    job_applies_count INTEGER,
    other_interactions INTEGER
);

-- Create table: Chatbot_Prompts
CREATE TABLE Chatbot_Prompts (
    id SERIAL PRIMARY KEY,
    prompts TEXT
);

-- Create table: Current_Job_Openings
CREATE TABLE Current_Job_Openings (
    Job_id SERIAL PRIMARY KEY,
    Company TEXT,
    Role TEXT,
    Description TEXT,
    Salary NUMERIC,
    Location TEXT,
    Mode TEXT,
    employerid INTEGER REFERENCES Employer(id) -- Assuming there is an Employer table with an id column
);

-- Create table: freelancing
CREATE TABLE freelancing (
    freelancing_id SERIAL PRIMARY KEY,
    job_id INTEGER REFERENCES Current_Job_Openings(Job_id),
    project_budget NUMERIC,
    deadline DATE,
    required_skills TEXT
);

-- Create table: fulltimejobs
CREATE TABLE fulltimejobs (
    fulltimejob_id SERIAL PRIMARY KEY,
    job_id INTEGER REFERENCES Current_Job_Openings(Job_id),
    experience_required TEXT,
    benefits TEXT,
    start_date DATE
);

-- Create table: internships
CREATE TABLE internships (
    internship_id SERIAL PRIMARY KEY,
    job_id INTEGER REFERENCES Current_Job_Openings(Job_id),
    duration TEXT,
    stipend NUMERIC,
    start_date DATE,
    end_date DATE
);

-- Create table: Jobseeker_Social_Media_Links
CREATE TABLE Jobseeker_Social_Media_Links (
    jobseeker_id SERIAL PRIMARY KEY,
    github_url TEXT,
    linkedin_url TEXT
);

-- Create table: parttimejobs
CREATE TABLE parttimejobs (
    parttimejob_id SERIAL PRIMARY KEY,
    job_id INTEGER REFERENCES Current_Job_Openings(Job_id),
    hours_per_week INTEGER,
    hourly_rate NUMERIC,
    schedule TEXT
);

-- Create table: social_media_score
CREATE TABLE social_media_score (
    jobseeker_id SERIAL PRIMARY KEY,
    github_score INTEGER,
    linkedin_score INTEGER,
    FOREIGN KEY (jobseeker_id) REFERENCES Jobseeker_Social_Media_Links(jobseeker_id)
);
