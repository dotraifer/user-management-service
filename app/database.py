from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from app.configuration import Configurations

# Database URL from the configuration
DATABASE_URL = Configurations.database.url

# Create a new SQLAlchemy engine instance
engine = create_engine(DATABASE_URL, echo=True)

# Create a configured "Session" class
SessionLocal = sessionmaker(bind=engine, autoflush=False)

# Base class for our classes definitions
Base = declarative_base()


def get_db() -> sessionmaker:
    """
    Provide a transactional scope around a series of operations.

    This function yields a database session that can be used to interact with the database.
    It ensures that the session is properly closed after use.

    Yields:
        Session: A SQLAlchemy database session.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
