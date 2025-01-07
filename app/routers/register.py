import logging

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, database, models
from app.auth import hash_password

router = APIRouter()


@router.post("/")
def register(user: schemas.UserCreate, db: Session = Depends(database.get_db)):
    """
    Register a new user.

    This endpoint registers a new user by saving their information in the database.

    Args:
        user (schemas.UserCreate): The user creation data containing first name, last name, email, and password.
        db (Session, optional): The database session dependency.

    Raises:
        HTTPException: If the email is already registered, a 400 status code is returned.

    Returns:
        dict: A dictionary containing a success message.
    """
    if db.query(models.User).filter(models.User.email == user.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    new_user = models.User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    logging.debug(f"User {user.first_name} {user.last_name} registered successfully!")
    return {"message": f"User {user.first_name} {user.last_name} registered successfully!"}
