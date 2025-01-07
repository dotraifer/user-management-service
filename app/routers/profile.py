import logging

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import database, models, auth

router = APIRouter()


@router.get("/")
def get_profile(
        db: Session = Depends(database.get_db),
        current_user: dict = Depends(auth.get_current_user),
):
    """
    Retrieve the profile of the currently authenticated user.

    This endpoint fetches the profile information of the user who is currently authenticated.

    Args:
        db (Session, optional): The database session dependency.
        current_user (dict, optional): The currently authenticated user dependency.

    Returns:
        dict: A dictionary containing the user's profile information.
    """
    db_user: models.User = db.query(models.User).filter(models.User.id == current_user["user_id"]).first()
    logging.debug(f"User {db_user.first_name} {db_user.last_name} retrieved their profile")
    return {db_user.__str__()}
