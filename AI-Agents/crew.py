import crewai
from crewai import Crew, Process
from agents import researcher, datascientist, softwareengineer
from tasks import research_task, datascientist_task, softwareengineer_task

# crew = Crew(
#     agents=[researcher, datascientist, softwareengineer],
#     tasks=[research_task, datascientist_task, softwareengineer_task],
#     process = Process.sequential,
# )
#
# result = crew.kickoff(inputs={"topic":"Does Data Science requires Competitive Programming as in CodeForces?"})
# print(result)
def result(topic):
    researcher_crew = Crew(
        agents = [researcher],
        tasks = [research_task],
        process = Process.sequential,
    )
    researcher_res = researcher_crew.kickoff(inputs={"topic":topic})

    datascientist_crew = Crew(
        agents = [datascientist],
        tasks = [datascientist_task],
        process = Process.sequential,
    )
    datascientist_res = datascientist_crew.kickoff(inputs={"topic":topic})

    softwareengineer_crew = Crew(
        agents=[softwareengineer],
        tasks=[softwareengineer_task],
        process=Process.sequential,
    )
    softwareengineer_res = softwareengineer_crew.kickoff(inputs={"topic":topic})

    res = {}
    res["Google Researcher"] = researcher_res
    res["Data Scientist Researcher"] = datascientist_res
    res["Software Engineer Researcher"] = softwareengineer_res

    return res