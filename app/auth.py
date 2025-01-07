import logging
from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi import HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# Secret key used for encoding and decoding JWT tokens
SECRET_KEY = "xpander.ai"
# Algorithm used for encoding JWT tokens
ALGORITHM = "HS256"
# Token expiration time in minutes
TOKEN_EXPIRATION_MINUTES = 30

# Password context for hashing and verifying passwords
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# Security scheme for HTTP Bearer authentication
security = HTTPBearer()


def hash_password(password: str) -> str:
    """
    Hash a plain password.

    Args:
        password (str): The plain password to hash.

    Returns:
        str: The hashed password.
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a plain password against a hashed password.

    Args:
        plain_password (str): The plain password to verify.
        hashed_password (str): The hashed password to verify against.

    Returns:
        bool: True if the password matches, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)


def create_token(data: dict) -> str:
    """
    Create a JWT token.

    Args:
        data (dict): The data to encode in the token.

    Returns:
        str: The encoded JWT token.
    """
    to_encode = data.copy()
    to_encode.update({"exp": datetime.utcnow() + timedelta(minutes=TOKEN_EXPIRATION_MINUTES)})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token: str) -> dict:
    """
    Decode a JWT token.

    Args:
        token (str): The JWT token to decode.

    Raises:
        HTTPException: If the token is invalid or expired.

    Returns:
        dict: The decoded token data.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> dict:
    """
    Get the currently authenticated user.

    Args:
        credentials (HTTPAuthorizationCredentials, optional): The HTTP Bearer token credentials.

    Returns:
        dict: The decoded token data representing the current user.
    """
    return decode_token(credentials.credentials)
