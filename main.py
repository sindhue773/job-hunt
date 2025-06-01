from job_search.crew import JobHunter
from langchain_google_genai import ChatGoogleGenerativeAI
import asyncio
from dotenv import load_dotenv
import os

load_dotenv()

def run(job_title: str = "Software Engineer",
        location: str = "San Francisco, CA",
        experience_level: str = "Mid-Level",
        industry: str = "Technology",
        skills: str = "Python, JavaScript, React"):
    
    try:
      

        inputs = {
            "job_title": job_title,
            "location": location,
            "experience_level": experience_level,
            "industry": industry,
            "skills": skills,
         }

        s= JobHunter().crew().kickoff(inputs=inputs)
        print("Job hunt initiated successfully!")
        print(s)
        return s

    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    run(job_title="Software Engineer",
        location="San Francisco, CA",
        experience_level="Mid-Level",
        industry="Technology",
        skills="Python, JavaScript, React")