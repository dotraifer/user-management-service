from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    """
    Schema for creating a new user.

    Attributes:
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        email (EmailStr): The email address of the user.
        password (str): The password for the user.
    """
    first_name: str
    last_name: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    """
    Schema for user login.

    Attributes:
        email (EmailStr): The email address of the user.
        password (str): The password for the user.
    """
    email: EmailStr
    password: str


class UserUpdate(BaseModel):
    """
    Schema for updating user information.

    Attributes:
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        email (EmailStr): The email address of the user.
    """
    first_name: str
    last_name: str
    email: EmailStr
