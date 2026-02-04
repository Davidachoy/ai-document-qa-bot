from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Doc Q&A API"
    debug: bool = True

    database_url: str = "postgresql+asyncpg://docqa_user:docqa_pass@localhost:5432/docqa"

    chroma_host: str = "localhost"
    chroma_port: int = 8001

    openai_api_key: str
    openai_embedding_model: str = "text-embedding-3-small"

    class Config:
        env_file = ".env"


settings = Settings()
