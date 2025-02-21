from fastapi import APIRouter, Depends, HTTPException, status
from . import auth 

api_router = APIRouter()
api_router.include_router(auth.authRouter, prefix="/auth", tags=["Auth"])
