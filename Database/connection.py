from pymongo import MongoClient
import os
from pathlib import Path
from dotenv import load_dotenv

# Load .env from backend directory regardless of cwd
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

url = os.getenv("MongoDbUrl")

connectionstring = MongoClient(url)
DatabaseName = connectionstring["student_management"]

collectionName = DatabaseName["studentList"]