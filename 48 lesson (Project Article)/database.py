from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

database_url = "sqlite:///data.db"
engine = create_engine(database_url, echo=True)
SessionLocal = sessionmaker(bind=engine)
