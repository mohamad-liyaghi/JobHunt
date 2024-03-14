from fastapi import APIRouter
from .auth import router as auth_router
from .profiles import router as profiles_router

v1_router = APIRouter()

v1_router.include_router(auth_router, prefix="/auth")
v1_router.include_router(profiles_router, prefix="/profiles")
