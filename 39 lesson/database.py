import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker

load_dotenv()
database_url = os.getenv("URL")
engine = create_engine(url=database_url, echo=True)
Session = sessionmaker(bind=engine)
