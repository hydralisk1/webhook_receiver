import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

port = int(os.getenv('PORT'))

if __name__ == "__main__":
    uvicorn.run("app.api:app", host="0.0.0.0", port=port, reload=True)