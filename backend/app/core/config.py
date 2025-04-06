from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    weaviate_url: str

    class Config:
        env_file = ".env"

settings = Settings()
