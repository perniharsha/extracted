from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DB_URL = os.getenv("DB_URL", "mysql+pymysql://admin:Harshaamity@database-1.cr0uyqcu644u.us-east-1.rds.amazonaws.com/surveydb")

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
