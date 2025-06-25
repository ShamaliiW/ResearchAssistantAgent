# Exposing as Fast API to Test locally

from fastapi import FastAPI
from pydantic import BaseModel
from app.crew import build_crew
# from app.main import build_crew

import openai
import os 

from dotenv import load_dotenv

# # Read secrets from the Key Vault
# from azure.identity import DefaultAzureCredential
# from azure.keyvault.secrets import SecretClient

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OpenAI API key not found. Please set OPENAI_API_KEY in the environment.")
openai.api_key = OPENAI_API_KEY

app = FastAPI()

class ResearchRequest(BaseModel):
    company_name: str

@app.get("/")
def read_root():
    return {"status": "Research Assistant API running"}

@app.get("/health")
def read_health():
    return {"200": "ok"}

@app.post("/research")
def research(request: ResearchRequest):
    company_name = request.company_name
    crew = build_crew(company_name)
    result = crew.kickoff(inputs={"company_name": company_name})
    return {"result": result}