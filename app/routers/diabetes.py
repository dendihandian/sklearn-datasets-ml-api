from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

@router.get("/diabetes/predict", tags=["diabetes"])
async def diabetes_predict():

    # go here

    return {
        'target': 78.0
    }
