pip install "fastapi[standard]"
git rm -r --cached .venv


# def get_openai_api_key():
#     key_vault_name = os.getenv("KEY_VAULT_NAME")
#     if not key_vault_name:
#         raise ValueError("KEY_VAULT_NAME environment variable not set")

#     kv_uri = f"https://{key_vault_name}.vault.azure.net"
#     credential = DefaultAzureCredential()
#     client = SecretClient(vault_url=kv_uri, credential=credential)
#     return client.get_secret("OPENAI-API-KEY").value

# @app.on_event("startup")
# def setup_openai():
#     try:
#         openai.api_key = get_openai_api_key()
#         print("OPENAI API key successfully set from key vault")
#     except Exception as e:
#         print("Failed to fetch OpenAI API key {e}")
#         raise
