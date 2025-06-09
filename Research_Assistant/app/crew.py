import os
from crewai import Crew, Process, LLM
from agents import get_content_writer, get_research_analyst
from tasks import get_research_task, get_analysis_task

from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

llm = LLM(model="gpt-4o")

def build_crew(company_name):
    research_analyst = get_research_analyst(company_name, llm)
    content_writer = get_content_writer(llm)

    research_task = get_research_task(company_name, research_analyst)
    analysis_task = get_analysis_task(content_writer, research_task)
    
    crew  = Crew(
        agents = [research_analyst, content_writer],
        tasks = [research_task, analysis_task],
        process = Process.sequential,
        memory =True,
        cache = True,
        max_rpm = 100,
        share_crew = True,
        verbose = True
    )

    return crew

