from fastapi import APIRouter
from src.api.v1.auth.route import auth_router

router = APIRouter(prefix="/api/v1/facebook-meta-ads")

router.include_router(auth_router, tags=['Auth'])
