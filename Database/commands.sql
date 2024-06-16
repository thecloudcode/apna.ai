CREATE TABLE Users (
    User_id SERIAL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    Phone_Number VARCHAR(15),
    User_Type VARCHAR(50) NOT NULL CHECK (User_Type IN ('Employer', 'Jobseeker'))
);

CREATE TABLE Employers (
    Employer_id SERIAL PRIMARY KEY,
    User_id INT NOT NULL,
    Company_Name VARCHAR(100) NOT NULL,
    FOREIGN KEY (User_id) REFERENCES Users(User_id) ON DELETE CASCADE
);

CREATE TABLE Jobseekers (
    Jobseeker_id SERIAL PRIMARY KEY,
    User_id INT NOT NULL,
    Resume TEXT,
    FOREIGN KEY (User_id) REFERENCES Users(User_id) ON DELETE CASCADE
);

CREATE TABLE Applications (
    Application_id SERIAL PRIMARY KEY,
    Jobseeker_id INT NOT NULL,
    Job_id INT NOT NULL,
    Date_Applied DATE NOT NULL,
    Status VARCHAR(50) NOT NULL,
    FOREIGN KEY (Jobseeker_id) REFERENCES Jobseekers(Jobseeker_id) ON DELETE CASCADE,
    FOREIGN KEY (Job_id) REFERENCES Current_Job_Openings(Job_id) ON DELETE CASCADE
);

CREATE TABLE Current_Job_Openings (
    Job_id SERIAL PRIMARY KEY,
    Company VARCHAR(100) NOT NULL,
    Role VARCHAR(100) NOT NULL,
    Description TEXT,
    Salary DECIMAL(10, 2),
    Location VARCHAR(100),
    Mode VARCHAR(50) CHECK (Mode IN ('Onsite', 'Remote', 'Hybrid'))
);

CREATE TABLE Fact_Table (
    Fact_id SERIAL PRIMARY KEY,
    User_id INT NOT NULL,
    Job_id INT NOT NULL,
    Application_id INT NOT NULL,
    FOREIGN KEY (User_id) REFERENCES Users(User_id) ON DELETE CASCADE,
    FOREIGN KEY (Job_id) REFERENCES Current_Job_Openings(Job_id) ON DELETE CASCADE,
    FOREIGN KEY (Application_id) REFERENCES Applications(Application_id) ON DELETE CASCADE
);

CREATE TABLE Applicants_Rating_Data (
    Id SERIAL PRIMARY KEY,
    "101" FLOAT,
    "102" FLOAT,
    "103" FLOAT,
    "104" FLOAT,
    "105" FLOAT,
    "106" FLOAT,
    "107" FLOAT,
    "108" FLOAT,
    "109" FLOAT,
    "110" FLOAT,
    "111" FLOAT,
    "112" FLOAT,
    "113" FLOAT,
    "114" FLOAT,
    "115" FLOAT,
    "116" FLOAT,
    "117" FLOAT,
);
