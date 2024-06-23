<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Project Overview</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f0f0f0;
            padding: 20px;
        }

        .container {
            max-width: 800px;
            margin: auto;
            background: #fff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        h1,
        h2,
        h3 {
            color: #333;
            margin-bottom: 20px;
        }

        p {
            color: #666;
        }

        .table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }

        .table th,
        .table td {
            border: 1px solid #ddd;
            padding: 10px;
            text-align: left;
        }

        .table th {
            background-color: #f2f2f2;
            font-weight: bold;
        }

        code {
            background-color: #f9f9f9;
            padding: 3px 5px;
            border: 1px solid #ccc;
            border-radius: 3px;
        }

        .highlight {
            background-color: #ffffcc;
        }

        .note {
            background-color: #f0f8ff;
            padding: 10px;
            margin-top: 20px;
            border-left: 3px solid #87ceeb;
        }
    </style>
</head>

<body>
    <div class="container">
        <header>
            <h1>Project Overview</h1>
        </header>

        <section>
            <h2>Database Overview</h2>
            <p>Description of various database tables and relationships:</p>

            <h3>Tables and Relationships</h3>

            <table class="table">
                <thead>
                    <tr>
                        <th>Table Name</th>
                        <th>Description</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Activity_Scorer</td>
                        <td>Tracks user activities such as chatbot interactions, website visits, and job applications.</td>
                    </tr>
                    <tr>
                        <td>Chatbot_Prompts</td>
                        <td>Stores prompts used by the chatbot for interaction.</td>
                    </tr>
                    <tr>
                        <td>Current_Job_Openings</td>
                        <td>Contains information about current job openings.</td>
                    </tr>
                    <tr>
                        <td>freelancing</td>
                        <td>Records freelancing opportunities with project details.</td>
                    </tr>
                    <tr>
                        <td>fulltimejobs</td>
                        <td>Stores full-time job listings with detailed information.</td>
                    </tr>
                    <tr>
                        <td>internships</td>
                        <td>Lists internships available with duration and stipend details.</td>
                    </tr>
                    <tr>
                        <td>parttimejobs</td>
                        <td>Provides details on part-time job opportunities.</td>
                    </tr>
                    <tr>
                        <td>Jobseeker_Social_Media_Links</td>
                        <td>Manages social media links for job seekers.</td>
                    </tr>
                    <tr>
                        <td>social_media_score</td>
                        <td>Stores social media scores for job seekers.</td>
                    </tr>
                </tbody>
            </table>

            <div class="note">
                <p><strong>Note:</strong> Foreign key relationships are established between tables for data consistency and integrity.</p>
            </div>
        </section>

        <section>
            <h2>Creating the Chatbot</h2>
            <p>Description of the chatbot implementation:</p>

            <h3>Technology Used</h3>
            <p>Implemented using Python and third-party libraries.</p>

            <h3>Implementation Steps</h3>
            <ol>
                <li>Design chatbot prompts and user responses.</li>
                <li>Develop chatbot logic using Python.</li>
                <li>Test iteratively with sample interactions.</li>
                <li>Deploy and integrate with the web application.</li>
            </ol>
        </section>

        <section>
            <h2>Web Scraping Application for Activity Scoring</h2>
            <p>Description of the web scraping application:</p>

            <h3>Purpose</h3>
            <p>Retrieve data from specified web sources and analyze user activities.</p>

            <h3>Key Features</h3>
            <ul>
                <li>Utilizes Python, BeautifulSoup, and Scrapy for data extraction.</li>
                <li>Automated to run periodically for continuous data updates.</li>
                <li>Computes scores based on predefined algorithms and updates Activity_Scorer.</li>
            </ul>
        </section>

        <section>
            <h2>Email Automation Based on User Activities</h2>
            <p>Description of email automation based on user activities:</p>

            <h3>Functionality</h3>
            <ul>
                <li>Activated by significant user actions or score thresholds.</li>
                <li>Sends personalized emails based on user data and scores.</li>
                <li>Utilizes SMTP protocols for reliable email delivery.</li>
            </ul>

            <h3>Implementation Steps</h3>
            <ol>
                <li>Setup email server credentials for integration.</li>
                <li>Connect with the web application and activity tracking system.</li>
                <li>Design customizable email templates for various scenarios.</li>
            </ol>
        </section>

        <footer>
            <p>For more details, refer to the <code>README.md</code> file in this repository.</p>
        </footer>
    </div>
</body>

</html>
