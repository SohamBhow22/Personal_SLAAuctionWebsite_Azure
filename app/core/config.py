import os
import urllib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Azure SQL Database details from environment
AZURE_DB_SERVER = os.getenv("AZURE_DB_SERVER")
AZURE_DB_NAME = os.getenv("AZURE_DB_NAME")

# Authenticate using Entra ID
credential = DefaultAzureCredential()
access_token = credential.get_token("https://database.windows.net/").token
encoded_token = urllib.parse.quote_plus(f"Bearer {access_token}")

# Create connection string for SQLAlchemy
DATABASE_URL = f"mssql+pyodbc://@{AZURE_DB_SERVER}/{AZURE_DB_NAME}?driver=ODBC+Driver+18+for+SQL+Server&access_token={encoded_token}"

# Database engine and session factory
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency function
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
