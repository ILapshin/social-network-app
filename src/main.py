from fastapi import FastAPI

from . import models
from .database import engine
from .routers import (
    users,
    posts,
    reactions
)

app = FastAPI()

app.include_router(users.router)
app.include_router(posts.router)
app.include_router(reactions.router)

models.Base.metadata.create_all(engine)