import uvicorn
from fastapi import FastAPI

from infrastructure.config.app import APP_OPTIONS
from infrastructure.router import api_router

app = FastAPI(
    title=APP_OPTIONS.project_name,
    description="",
    version="1.0.0"
)

app.include_router(api_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=5000, workers=1, debug=False)