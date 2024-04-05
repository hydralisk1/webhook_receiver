import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

def get_database():
    CONNECTION_STRING = f"mongodb+srv://{os.getenv('MONGODB_ACCOUNT')}:{os.getenv('MONGDODB_PASSWORD')}@{os.getenv('DB_HOST')}/?retryWrites=true&w=majority&appName=@{os.getenv('APP_NAME')}"
    client = MongoClient(CONNECTION_STRING)

    return client['mydatabase']
