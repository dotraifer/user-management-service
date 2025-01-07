from functools import lru_cache
from app.database import get_db
from sqlalchemy.orm import Session
from app import models


@lru_cache(maxsize=200)
def get_cached_user(user_id: int, db: Session):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        return db_user
    return None


def invalidate_cache():
    get_cached_user.cache_clear()
