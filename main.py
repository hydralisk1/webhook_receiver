from fastapi import FastAPI

app = FastAPI()

@app.webhooks.post('/')
def home():
    return { "Hello": "World" }
