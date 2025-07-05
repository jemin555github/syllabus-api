from fastapi import APIRouter
from src.api.v1.auth.route import auth_router
from src.api.v1.medias.route import media_router

router = APIRouter(prefix="/api/v1/facebook-meta-ads")

router.include_router(auth_router, tags=['Auth'])
router.include_router(media_router, tags=['Media'])

