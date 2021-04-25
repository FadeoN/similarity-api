from fastapi import APIRouter

from infrastructure.controller.index import router as index_router
from infrastructure.controller.search import router as search_router

api_router = APIRouter()


api_router.include_router(index_router, prefix="/index", tags=["index"])
api_router.include_router(search_router, prefix="/search", tags=["search"])