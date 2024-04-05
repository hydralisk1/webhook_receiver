from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def get_home():
    return { "Hello": "World Post" }

@app.post('/')
def post_home():
    return { "Hello": "World Post" }
