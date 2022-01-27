from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

@router.get("/iris/predict", tags=["iris"])
async def iris_predict():

    # go here

    return {
        'target': 1
    }
