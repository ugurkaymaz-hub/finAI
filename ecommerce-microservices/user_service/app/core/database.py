from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
import os


# SQLAlchemy veritabanı bağlantı URL'sini al
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

# SQLAlchemy engine oluştur
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Session fabrikası oluştur
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base model oluştur
Base = declarative_base()

# Database bağlantı fonksiyonu
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

