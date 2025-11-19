from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Fullstack Workboard API"
    environment: str = "local"
    database_url: str = "postgresql://workboard_user:password@localhost:5432/workboard"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
