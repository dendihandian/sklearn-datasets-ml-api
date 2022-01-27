# from typing import Optional
from fastapi import FastAPI
from app.routers import iris, diabetes
from app import __version__


app = FastAPI()

app.include_router(iris.router)
app.include_router(diabetes.router)


@app.get("/")
def read_root():
    return {
        "message": "Welcome to Sklearn Datasets ML API",
        "version": __version__
    }
