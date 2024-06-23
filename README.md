<h3 align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.herokuapp.com/?lines=Project+Overview....;Let+Gooooo...+!&center=true&size=35">
  </a>
</h3>


## Database Overview

### Tables and Relationships

- **Activity_Scorer**
  - Tracks user activities such as chatbot interactions, website visits, and job applications.
  
- **Chatbot_Prompts**
  - Stores prompts used by the chatbot for interaction.
  
- **Current_Job_Openings**
  - Contains information about current job openings, including company, role, description, salary, location, and mode of work.
  
- **freelancing**
  - Records freelancing opportunities with project budget, deadline, and required skills.
  
- **fulltimejobs**
  - Stores full-time job listings with details on required experience, benefits, and start date.
  
- **internships**
  - Lists internships available, specifying duration, stipend, start date, and end date.
  
- **parttimejobs**
  - Provides details on part-time job opportunities, such as hours per week, hourly rate, and schedule.
  
- **Jobseeker_Social_Media_Links**
  - Manages social media links for job seekers, including GitHub and LinkedIn URLs.
  
- **social_media_score**
  - Stores social media scores for job seekers, specifically GitHub and LinkedIn scores.
  
**Foreign Key Relationships:**
- Tables like `freelancing`, `fulltimejobs`, `internships`, `parttimejobs`, and `social_media_score` reference `Current_Job_Openings` for job ID association.
- `Jobseeker_Social_Media_Links` and `social_media_score` are interconnected by the `jobseeker_id` field.

## Creating the Chatbot

### Technology Used
- Implemented using Python and third-party libraries.

### Implementation Steps
1. Design chatbot prompts and user responses.
2. Develop logic using Python.
3. Test iteratively with sample interactions.
4. Deploy and integrate with the web application for seamless user engagement.

## Web Scraping Application for Activity Scoring

### Purpose
- Retrieve data from specified web sources.
- Analyze user activities like job searches, site visits, and engagement levels.

### Key Features
- Technologies: Utilizes Python, BeautifulSoup, and Scrapy for data extraction.
- Automated to run periodically for continuous data updates.
- Computes scores based on predefined algorithms and updates `Activity_Scorer`.

## Email Automation Based on User Activities

### Functionality
- Triggered by significant user actions or score thresholds.
- Sends personalized emails based on user data and scores.
- Utilizes SMTP protocols for reliable email delivery.

### Implementation Steps
1. Setup email server credentials.
2. Integrate with the web application and activity tracking system.
3. Design customizable email templates for various scenarios.

---

For more details, refer to the documentation and code files in this repository.
