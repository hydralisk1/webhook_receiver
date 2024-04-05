from fastapi import FastAPI, Request
from .db import get_database
from pymongo import DESCENDING

app = FastAPI()
dbname = get_database()
collection_name = dbname["heyflow"]

@app.post('/')
async def post_home(request: Request):
    data = await request.json()
    collection_name.delete_many({})
    collection_name.insert_one(data)
    return { "message": "Data inserted successfully" }

@app.get('/')
def get_home():
    value = [v for v in collection_name.find({}, {"_id": 0})][0]
    return value
