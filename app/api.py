from fastapi import FastAPI

app = FastAPI()

@app.get('/', tags=["Root"])
async def read_root():
    return { "Hello": "World Get" }

@app.post('/')
async def post_home():
    return { "Hello": "World Post" }
