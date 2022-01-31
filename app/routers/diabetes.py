from fastapi import APIRouter
from pydantic import BaseModel
import pickle

model = pickle.load(open('./app/artifacts/diabetes/model.pkl', 'rb'))

class DiabetesFeatures(BaseModel):
    age: float
    sex: float
    bmi: float
    bp: float
    s1: float
    s2: float
    s3: float
    s4: float
    s5: float
    s6: float


router = APIRouter()

@router.post("/diabetes/predict", tags=["diabetes"])
async def diabetes_predict(param: DiabetesFeatures):

    prediction = model.predict([[
        param.__getattribute__('age'),
        param.__getattribute__('sex'),
        param.__getattribute__('bmi'),
        param.__getattribute__('bp'),
        param.__getattribute__('s1'),
        param.__getattribute__('s2'),
        param.__getattribute__('s3'),
        param.__getattribute__('s4'),
        param.__getattribute__('s5'),
        param.__getattribute__('s6'),
    ]])

    return {
        'target': prediction[0][0]
    }
