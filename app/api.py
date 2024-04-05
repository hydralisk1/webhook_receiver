from fastapi import FastAPI, Request
from .db import get_database

app = FastAPI()
dbname = get_database()
collection_name = dbname["heyflow"]

@app.post('/')
async def post_home(request: Request):
    data = await request.json()
    collection_name.insert_one(data)
    return await request.json()

@app.get('/')
async def get_home():
    return [i for i in collection_name.find()]
