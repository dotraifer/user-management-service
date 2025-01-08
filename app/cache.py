from functools import lru_cache
from app.database import get_db
from sqlalchemy.orm import Session
from app import models


@lru_cache(maxsize=200)
def get_cached_user(user_id: int, db: Session):
    """
    Retrieve a cached user from the database.

    This function uses an LRU (Least Recently Used) cache to store up to 200 user queries.
    If the user is found in the cache, it is returned directly. Otherwise, a database query is performed.

    Args:
        user_id (int): The ID of the user to retrieve.
        db (Session): The database session used to query the user.

    Returns:
        models.User: The user object if found, otherwise None.
    """
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        return db_user
    return None


def invalidate_cache():
    """
    Invalidate the user cache.

    This function clears the LRU cache, removing all cached user queries.
    """
    get_cached_user.cache_clear()
