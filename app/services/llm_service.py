from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("google_api_key")
planner_llm = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", google_api_key=api_key)
worker_llm = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", google_api_key=api_key)