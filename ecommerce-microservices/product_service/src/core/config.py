#Library imports
from pydantic_settings import BaseSettings

#Local imports
import os
from dotenv import load_dotenv


load_dotenv()

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM")

settings = Settings()