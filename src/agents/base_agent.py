"""
Base agent class for interview agents.
"""
from typing import Dict, Any
from langchain_openai import AzureChatOpenAI
from config import settings


class BaseAgent:
    """Base class for all interview agents."""
    
    def __init__(self):
        """Initialize the base agent."""
        self.llm = self._create_llm()
    
    def _create_llm(self) -> AzureChatOpenAI:
        """
        Create an Azure OpenAI LLM instance.
        
        Returns:
            AzureChatOpenAI: Configured LLM instance
        """
        return AzureChatOpenAI(
            azure_endpoint=settings.OPENAI_ENDPOINT,
            azure_deployment=settings.OPENAI_DEPLOYMENT_NAME,
            api_version=settings.OPENAI_API_VERSION,
            api_key=settings.OPENAI_API_KEY,
            temperature=settings.TEMPERATURE,
        )
    
    def generate_question(self, prompt: str) -> str:
        """
        Generate a question using the LLM.
        
        Args:
            prompt: The prompt to use for generation
            
        Returns:
            str: Generated question
        """
        response = self.llm.invoke(prompt)
        return response.content
