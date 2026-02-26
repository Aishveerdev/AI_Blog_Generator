from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama

from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
load_dotenv()

api_key1 = os.getenv("google_api_key1")
api_key2 = os.getenv("google_api_key2")
api_key3 = os.getenv("openai_api_key")

planner_llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=api_key1)
worker_llm = ChatOllama(model="phi3",temperature=0.3)


