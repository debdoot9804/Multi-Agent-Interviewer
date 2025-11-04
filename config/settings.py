"""
Configuration settings for the AI Interviewer application.
"""
import os
from typing import Optional
from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # Azure OpenAI Configuration
    azure_openai_api_key: str = Field(..., alias="AZURE_OPENAI_API_KEY")
    azure_openai_endpoint: str = Field(..., alias="AZURE_OPENAI_ENDPOINT")
    azure_openai_deployment_name: str = Field(..., alias="AZURE_OPENAI_DEPLOYMENT_NAME")
    azure_openai_api_version: str = Field(
        default="2024-02-15-preview", 
        alias="AZURE_OPENAI_API_VERSION"
    )
    
    # Interview Configuration
    max_technical_questions: int = Field(default=6, alias="MAX_TECHNICAL_QUESTIONS")
    max_hr_questions: int = Field(default=3, alias="MAX_HR_QUESTIONS")
    max_manager_questions: int = Field(default=2, alias="MAX_MANAGER_QUESTIONS")
    
    # Model Configuration
    temperature: float = Field(default=0.7, alias="TEMPERATURE")
    max_tokens: int = Field(default=500, alias="MAX_TOKENS")
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


def get_settings() -> Settings:
    """
    Get application settings instance.
    
    Returns:
        Settings: Application settings
    """
    return Settings()
