from fastapi import APIRouter
from pydantic import BaseModel
import pickle

model = pickle.load(open('./app/artifacts/iris/model.pkl', 'rb'))

class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

router = APIRouter()

@router.post("/iris/predict", tags=["iris"])
async def iris_predict(param: IrisFeatures):

    prediction = model.predict([[
        param.__getattribute__('sepal_length'),
        param.__getattribute__('sepal_width'),
        param.__getattribute__('petal_length'),
        param.__getattribute__('petal_width'),
    ]])

    return {
        'target': prediction[0]
    }
