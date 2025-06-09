from fastapi import FastAPI
from pydantic import BaseModel
from main import build_crew

import openai
import os 

# Read secrets from the Key Vault
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

app = FastAPI()

def get_openai_api_key():
    key_vault_name = os.getenv("KEY_VAULT_NAME")
    if not key_vault_name:
        raise ValueError("KEY_VAULT_NAME environment variable not set")

    kv_uri = f"https://{key_vault_name}.vault.azure.net"
    credential = DefaultAzureCredential()
    client = SecretClient(vault_url=kv_uri, credential=credential)
    return client.get_secret("OPENAI-API-KEY")

@app.on_event("startup")
def setup_openai():
    try:
        openai_api_key = get_openai_api_key()
        print("OPENAI API key successfully set from key vault")
    except Exception as e:
        print("Failed to fetch OpenAI API key {e}")
        raise


class ResearchRequest(BaseModel):
    company_name: str

@app.get("/")
def read_root():
    return {"status": "Research Assistant API running"}


@app.post("/research")
def research(request: ResearchRequest):
    company_name = request.company_name
    crew = build_crew(company_name)
    result = crew.kickoff(inputs={"company_name": company_name})
    return {"result": result}