import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, database, models, auth

router = APIRouter()


@router.post("/")
def login(user: schemas.UserLogin, db: Session = Depends(database.get_db)):
    """
    Handle user login.

    This endpoint verifies the user's credentials and returns an authentication token if the credentials are valid.

    Args:
        user (schemas.UserLogin): The user login data containing email and password.
        db (Session, optional): The database session dependency.

    Raises:
        HTTPException: If the credentials are invalid, a 401 status code is returned.

    Returns:
        dict: A dictionary containing the authentication token.
    """
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not db_user or not auth.verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = auth.create_token({"user_id": db_user.id})
    logging.debug(f"User {db_user.first_name} {db_user.last_name} logged in successfully!")
    return {"token": token}
