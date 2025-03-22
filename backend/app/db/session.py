from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.app.db.base import Base
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, connect_args={"charset": "utf8mb4"})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine )

def create_db():
    Base.metadata.create_all(bind=engine)