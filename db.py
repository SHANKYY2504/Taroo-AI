from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os


# SQLALCHEMY_DATABASE_URL=os.getenv('DATABASE_URL')
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:shajh%4069@localhost:5432/tarooai"

if not SQLALCHEMY_DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set.")

engine=create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_table():
    Base.metadata.create_all(bind=engine)
