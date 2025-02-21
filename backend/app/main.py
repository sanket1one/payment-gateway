from fastapi import FastAPI , Depends
from contextlib import asynccontextmanager
from app.utils.init_db import create_tables
from app.utils.protectRoute import get_current_user
from app.db.schemas.user import UserOutput
from app.routers import api_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize DB at Start
    create_tables()
    yield # Seperation point


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)


@app.get("/")
async def root():
    return {"message": "Hello Sanket"}


@app.get("/protected")
def read_protected(user: UserOutput = Depends(get_current_user)):
    return {"data": user}
