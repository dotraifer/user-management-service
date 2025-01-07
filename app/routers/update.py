import logging

from fastapi import APIRouter, Depends, HTTPException
from app import schemas, database, models, auth
from sqlalchemy.orm import Session
from app.cache import invalidate_cache

router = APIRouter()


@router.put("/")
def update(user: schemas.UserUpdate, db: Session = Depends(database.get_db),
           current_user: dict = Depends(auth.get_current_user)):
    """
    Update user information.

    This endpoint allows the currently authenticated user to update their information.

    Args:
        user (schemas.UserUpdate): The user update data containing fields to be updated.
        db (Session, optional): The database session dependency.
        current_user (dict, optional): The currently authenticated user dependency.

    Raises:
        HTTPException: If the user is not found, a 404 status code is returned.

    Returns:
        dict: A dictionary containing a success message.
    """
    logging.error(f"User {current_user} is updating their information")
    db_user = db.query(models.User).filter(models.User.id == current_user["user_id"]).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    for key, value in user.dict(exclude_unset=True).items():
        setattr(db_user, key, value)

    db.commit()
    invalidate_cache()  # Invalidate the cache to reflect the updated user information
    logging.debug(f"User {db_user.first_name} {db_user.last_name} updated successfully!")
    return {"message": "User information updated successfully!"}
