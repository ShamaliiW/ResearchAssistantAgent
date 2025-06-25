from crewai import Task
from app.tools import search_tool
from app.agents import get_research_analyst, get_content_writer, get_prospect_researcher

# Research Task
def get_research_task(company_name, agent):
    return Task(
        description=f"""
            Conduct an in-depth company research on: {company_name}
        
            Follow these steps:
            1. Use reliable sources (official websites, news articles, LinkedIn, Crunchbase, etc.)
            2. Identify and extract key company details: overview, services, tech stack, leadership, financials, partnerships
            3. Analyze strategic direction, market focus, recent developments, and potential software development needs
            4. Cross-verify important facts across multiple sources
            5. Document all findings clearly with citations
        """,
        agent=agent,
        expected_output="""
            A comprehensive company research report that includes:
            - Executive Summary of key insights
            - Company Overview (location, size, industry, founding year, website)
            - Key Personnel (CEO, CTO, etc.)
            - Services & Offerings
            - Technology Stack used (frontend/backend/cloud/AI)
            - Recent News & Milestones (with dates and sources)
            - Partnerships, Clients, and Funding (if available)
            - Strategic Focus and Potential Pain Points
            - Opportunities for Custom Software Collaboration
            - Verified Facts and Statistics (with references)
            - All citations and clickable source links
        
            Please format the output in well-organized sections using bullet points and subheadings for easy reference.
        """,
    tool = [search_tool],
    async_execution = False
    )

    # Analysis Task
def get_analysis_task(agent, task):
    return Task(
        description=f"""
            Synthesize the findings from the company research report  about the company received from the context into a concise, persuasive, and structured summary.
        
            Focus on:
            1. Highlighting key company facts and strategic goals
            2. Identifying technology gaps or growth opportunities
            3. Recommending angles for outreach based on their business needs
            4. Writing in a tone suitable for B2B proposal or cold outreach
        """,
        agent=agent,
        context=[task],
        expected_output="""
            A summarized company brief that includes:
            - Executive summary (2-3 paragraphs)
            - Key facts & insights (bulleted)
            - Potential challenges or areas for improvement
            - Suggested outreach angle or collaboration opportunity
            - Call-to-action statement for marketing team

            Output should be clean, well-organized, and ready to plug into an email or pitch deck.
        """,
    async_execution = False,
    output_file = 'company-research.md'
    )


    # Research Prospect Companies 
def get_prospect_list_task(agent):
    return Task(
        description=(
            "Generate a list of at least 50 companies around the world that are likely to need software development services. "
            "Target sectors may include fintech, healthtech, edtech, logistics, AI startups, or companies recently funded. "
            "For each company, provide name, country, industry, funding stage (if available), and a one-line reason why they "
            "might need software services. Output in tabular format (Markdown)."
        ),
        expected_output="A Markdown table listing 10+ companies with relevant details.",
        tool = [search_tool],
        agent=agent,
        async_execution = True # execute in parallel to other tasks (since this is a seperate task and has no dependencies)
    )