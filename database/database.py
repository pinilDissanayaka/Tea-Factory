import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import find_dotenv, load_dotenv
from sqlalchemy.ext.declarative import declarative_base

load_dotenv(find_dotenv())

engine= create_engine(os.getenv('DB_URL'))      
     
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)

Base= declarative_base()

def get_db():
    """This function returns a database session instance."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()