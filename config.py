from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    OPENAI_API_KEY: Optional[str] = None
    PINECONE_API_KEY: Optional[str] = None
    TOKEN_SECRET: Optional[str] = None
    TAVILY_API_KEY: Optional[str] = None
    #CEREBRAS_API_KEY: Optional[str] = None
    GOOGLE_API_KEY: Optional[str] = None
    GROQ_API_KEY: Optional[str] = None

    """Loads the dotenv file. Including this is necessary to get
    pydantic to load a .env file."""
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
    # model_config = SettingsConfigDict(extra="ignore")