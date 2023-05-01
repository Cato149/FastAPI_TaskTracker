from fastapi import FastAPI
from fastapi_pagination import add_pagination

from api import tasks_router


app = FastAPI()
app.include_router(tasks_router)

add_pagination(app)