from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
async def get_home():
    return { "Hello": "World Post" }

@app.post('/')
async def post_home():
    return { "Hello": "World Post" }


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)