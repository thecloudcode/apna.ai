import crewai
from crewai import Task
from tools import research_tool
from agents import datascientist, researcher, softwareengineer

## Research
research_task = Task(
    description = (
        "Research on the {topic}."
        "Get detailed information about on the {topic}."
    ),
    expected_output = "A nearly 100 word answer to the {topic}",
    tools = [research_tool],
    agent = researcher
)

datascientist_task = Task(
    description = (
        "As a Data Scientist, get the details on the {topic}."
    ),
    expected_output = "Answer the {topic} in terms of data science in nearly 100 words",
    tools = [research_tool],
    agent = datascientist,
    async_execution = False,
    ouput_file = "output.md"
)

softwareengineer_task = Task(
    description = (
        "As a Software Engineer, answer on the topic {topic},"
    ),
    expected_output = "Answer the {topic} in terms of software engineering in nearly 100 words",
    tools = [research_tool],
    agent = softwareengineer,
    async_execution = False,
    ouput_file = "output2.md"
)

