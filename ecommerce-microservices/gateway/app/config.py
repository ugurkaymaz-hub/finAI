from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    JWT_SECRET_KEY: str = "-eYvjphieU0hVKwy34wsDsqwq05EEoH3IpdbQYf3PaI"
    JWT_ALGORITHM: str = "HS256"

    USER_SERVICE_URL: str = "http://user_service:8000"
    PRODUCT_SERVICE_URL: str = "http://product_service:8000"

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()