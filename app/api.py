from fastapi import FastAPI, Request

app = FastAPI()

@app.post('/')
async def post_home(request: Request):
    return await request.json()
