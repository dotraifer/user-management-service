import logging
import logging.config

import uvicorn
from fastapi import FastAPI

from app.database import Base, engine
from app.routers import register, login, update, profile

logging.config.fileConfig('logging.conf')

app = FastAPI()

app.include_router(register.router, prefix="/register")
app.include_router(login.router, prefix="/login")
app.include_router(update.router, prefix="/update")
app.include_router(profile.router, prefix="/profile")


def create_tables():
    logging.info("Creating tables")
    Base.metadata.create_all(bind=engine, checkfirst=True)


if __name__ == "__main__":
    logging.info("Starting server")
    create_tables()
    uvicorn.run(app, host="0.0.0.0", port=8000)
