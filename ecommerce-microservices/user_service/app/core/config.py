# app/core/config.py

import os
from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    API_PREFIX: str = "/api/v1"
    DEBUG: bool = False
    
    # Database
    DATABASE_URL: str = "postgresql://postgres:user_db_password@user_db:5432/user_db"
    
    # JWT
    JWT_SECRET_KEY: str = "-eYvjphieU0hVKwy34wsDsqwq05EEoH3IpdbQYf3PaI"
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()



