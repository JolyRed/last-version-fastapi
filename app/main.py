import logging
from fastapi import FastAPI
from routes import user_routes, task_routes

logging.basicConfig(level=logging.INFO)

app = FastAPI()
app.include_router(user_routes.router)
app.include_router(task_routes.router)
