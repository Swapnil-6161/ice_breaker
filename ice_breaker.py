from langchain_core.prompts import PromptTemplate
from google.auth import default
creds, project = default()
print("Project:", project)
print("Using service account:", getattr(creds, "service_account_email", "Not a service account"))
from langchain_google_vertexai import VertexAI
model = VertexAI(model_name="gemini-2.0-flash-lite-001")

message = "What are some of the pros and cons of Python as a programming language?"
print(model.invoke(message))