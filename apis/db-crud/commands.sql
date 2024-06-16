CREATE TABLE Users (
  UserID serial PRIMARY KEY,
  Email varchar(255) NOT NULL UNIQUE,
  PasswordHash varchar(255) NOT NULL,
  UserType varchar(10) NOT NULL CHECK (UserType IN ('JobSeeker', 'Employer', 'Admin')),
  CreatedDate TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  LastLoginDate TIMESTAMP NULL,
  Status varchar(8) NOT NULL CHECK (Status IN ('Active', 'Inactive', 'Banned')) DEFAULT 'Active'
);

CREATE TABLE JobSeekers (
    JobSeekerID INTEGER PRIMARY KEY,
    FirstName VARCHAR(100) NOT NULL,
    LastName VARCHAR(100) NOT NULL,
    Resume TEXT,
    ProfileSummary TEXT,
    Location VARCHAR(255),
    Skills TEXT,
    CONSTRAINT fk_jobseeker_user FOREIGN KEY (JobSeekerID) REFERENCES Users (UserID)
);

CREATE TABLE Employers (
    EmployerID INTEGER PRIMARY KEY,
    CompanyName VARCHAR(255) NOT NULL,
    CompanyDescription TEXT,
    Website VARCHAR(255),
    Location VARCHAR(255),
    ContactPhone VARCHAR(20),
    CONSTRAINT fk_employer_user FOREIGN KEY (EmployerID) REFERENCES Users (UserID)
);

