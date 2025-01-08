from app.database import Base
from sqlalchemy import Column, Integer, String


class User(Base):
    """
    Represents a user in the database.

    Attributes:
        id (int): The unique identifier for the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        email (str): The email address of the user.
        password (str): The hashed password of the user.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

    def __str__(self):
        """
        Returns a string representation of the user.

        Returns:
            str: A string containing the user's id, first name, last name, and email.
        """
        return f"id={self.id}, first_name={self.first_name}, last_name={self.last_name}, email={self.email}"
