from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

load_dotenv()

@CrewBase
class JobHunter:
    """JobHunter crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def job_search_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["job_search_agent"],
            verbose=True,
            tools=[SerperDevTool()],
        )

    @agent
    def resume_optimization_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["resume_optimization_agent"],
            verbose=True,
            tools=[SerperDevTool()],
        )

    @agent
    def interview_prep_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["interview_prep_agent"],
            verbose=True,
            tools=[SerperDevTool()],
        )

    @agent
    def market_research_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["market_research_agent"],
            verbose=True,
            tools=[SerperDevTool()],
        )

    @agent
    def application_tracker_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["application_tracker_agent"],
            verbose=True,
            tools=[SerperDevTool()],
        )

    @task
    def job_search_task(self) -> Task:
        return Task(
            config=self.tasks_config["job_search_task"],
            output_file="output/job_search_results.md",
        )

    @task
    def resume_optimization_task(self) -> Task:
        return Task(
            config=self.tasks_config["resume_optimization_task"],
            output_file="output/resume_optimization.md",
        )

    @task
    def interview_prep_task(self) -> Task:
        return Task(
            config=self.tasks_config["interview_prep_task"],
            output_file="output/interview_prep.md",
        )

    @task
    def market_research_task(self) -> Task:
        return Task(
            config=self.tasks_config["market_research_task"],
            output_file="output/market_research.md",
        )

    @task
    def application_tracking_task(self) -> Task:
        return Task(
            config=self.tasks_config["application_tracking_task"],
            output_file="output/application_tracking.md",
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )