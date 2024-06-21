import os
from crewai import Agent
from tools import research_tool
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                             verbose=True,
                             temperature=0.5,
                             google_api_key=os.getenv("GOOGLE_API_KEY"))

researcher = Agent(
    role = "Google Researcher",
    goal = "Research on the {topic} on Google",
    verbose = True,
    memory = True,
    backstory=(
        "You are an expert in researching on google, understanding technical stuff and an IT department recruiter"
    ),
    tools=[research_tool],
    llm=llm,
    allow_delegation=True
)

datascientist = Agent(
    role = "Data Scientist",
    goal = "Answer the {topic} as an Data Science Expert",
    verbose = True,
    memory = True,
    backstory=(
        "You are an expert in Data Science, Machine Learning, Python and you recruit data scientists"
    ),
    tools=[research_tool],
    llm = llm,
    allow_delegation=False
)

softwareengineer = Agent(
    role = "Software Engineer",
    goal = "Answer the {topic} as a Software Engineer",
    verbose = True,
    memory = True,
    backstory=(
        "You are an expert in Software Engineering, Programming, Coding, Data Structures and Algorithms"
    ),
    tools = [research_tool],
    llm = llm,
    allow_delegation = False
)


