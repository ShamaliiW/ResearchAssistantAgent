from crewai import Agent
from app.tools import search_tool

# Agent 1
def get_research_analyst(company_name, llm):
    return Agent(
        role = "Research Analyst from the web",
        goal = f"Conduct comprehensive research on a given {company_name} including its background, "
            "services, technology stack, recent news, key personnel, funding, partnerships, "
            "and strategic focus. Summarize findings into a clear, actionable report with references.",
        backstory="You are a seasoned research analyst with expertise in company profiling for strategic outreach. "
            "You specialize in gathering relevant, up-to-date, and credible information from various sources, "
            "including company websites, press releases, news articles, and tech blogs. "
            "Your output is used by marketing teams to tailor software development proposals.",
        allow_delegation = True,
        memory= True,
        vebose = True,
        tools = [search_tool],
        llm = llm
    )

# Agent 2
def get_content_writer(llm):
    return Agent(
        role = "Content Wrriter",
        goal = f"Analyze, synthesize, and transform company research findings about the company into clear, structured, and compelling narratives for outreach and proposal development.",
        backstory="You are an expert content strategist with a talent for distilling complex business research into concise, engaging content. "
            "You specialize in turning raw findings into executive summaries, opportunity briefs, and pitch-ready content. "
            "Your output helps marketing and sales teams craft personalized and informed outreach proposals.",
        allow_delegation = False,
        memory= True,
        vebose = True,
        llm = llm
    )

# Agent 3
def get_prospect_researcher(llm):
    return Agent(
        role="Prospect Research Analyst",
        goal="Identify and list global companies that may require custom software development services",
        backstory=(
            "You're an expert in business development and market research. "
            "You specialize in analyzing industries, funding patterns, and emerging tech trends to find companies that "
            "are likely in need of software development assistance."
        ),
        allow_delegation = False,
        memory= True,
        vebose = True,
        tools = [search_tool],
        llm = llm
    )