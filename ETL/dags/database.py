from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
from dotenv import load_dotenv, find_dotenv
import os


load_dotenv(find_dotenv())


engine=create_engine(url="mysql+mysqldb://root@localhost:3306/test")

Base=declarative_base()

local_session=sessionmaker(bind=engine, autocommit=False, autoflush=False)

session=local_session()
