import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./product.db")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your_secret")