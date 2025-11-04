"""
Base agent class for interview agents.
"""
from typing import Dict, Any
from langchain_openai import AzureChatOpenAI
from config.settings import Settings


class BaseAgent:
    """Base class for all interview agents."""
    
    def __init__(self, settings: Settings):
        """
        Initialize the base agent.
        
        Args:
            settings: Application settings
        """
        self.settings = settings
        self.llm = self._create_llm()
    
    def _create_llm(self) -> AzureChatOpenAI:
        """
        Create an Azure OpenAI LLM instance.
        
        Returns:
            AzureChatOpenAI: Configured LLM instance
        """
        return AzureChatOpenAI(
            azure_endpoint=self.settings.azure_openai_endpoint,
            azure_deployment=self.settings.azure_openai_deployment_name,
            api_version=self.settings.azure_openai_api_version,
            api_key=self.settings.azure_openai_api_key,
            temperature=self.settings.temperature,
            max_tokens=self.settings.max_tokens,
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
