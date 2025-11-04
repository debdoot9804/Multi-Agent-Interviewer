"""
Configuration settings for the AI Interviewer application.
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Azure OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_ENDPOINT = os.getenv("OPENAI_ENDPOINT")
OPENAI_DEPLOYMENT_NAME = os.getenv("OPENAI_CHAT_DEPLOYMENT_NAME")
OPENAI_API_VERSION = os.getenv("API_VERSION")

# Interview Configuration
MAX_TECHNICAL_QUESTIONS = int(os.getenv("MAX_TECHNICAL_QUESTIONS", "6"))
MAX_HR_QUESTIONS = int(os.getenv("MAX_HR_QUESTIONS", "3"))
MAX_MANAGER_QUESTIONS = int(os.getenv("MAX_MANAGER_QUESTIONS", "2"))

# Model Configuration
TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))

