from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
from dotenv import load_dotenv, find_dotenv
import os


load_dotenv(find_dotenv())

DATABASE_URL='postgresql://neondb_owner:npg_JNOti13AfaTV@ep-odd-water-a1vdqbo9-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require'

engine=create_engine(url=DATABASE_URL)

Base=declarative_base()

local_session=sessionmaker(bind=engine, autocommit=False, autoflush=False)

session=local_session()
