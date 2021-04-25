import uvicorn
from fastapi import FastAPI

from infrastructure.router import api_router

app = FastAPI(
    title="similarity-service",
    description="",
    version="1.0.0"
)

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, workers=3, debug=False)