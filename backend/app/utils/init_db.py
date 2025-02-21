from app.core.database import engine
from app.db.models.base import Base
from app.db.models.user import User

def create_tables():
    Base.metadata.create_all(bind=engine)