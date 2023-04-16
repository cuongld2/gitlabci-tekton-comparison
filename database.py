from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DB_HOST = os.getenv('DB_HOST').strip()
DB_USERNAME = os.getenv('DB_USERNAME').strip()
DB_PASSWORD = os.environ.get('DB_PASSWORD').strip()
DB_PORT = os.environ.get('DB_PORT').strip()
DB_NAME = os.environ.get('DB_NAME').strip()


SQLALCHEMY_DATABASE_URL = f"mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()





