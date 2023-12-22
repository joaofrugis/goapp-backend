from fastapi import APIRouter, HTTPException
from app.models.building import Building
from app.iamodels.pipeline import Pipeline
from typing import List

router = APIRouter()

@router.post("/predict", response_model=List[float])
async def post_predict(building: Building):
    pipeline = Pipeline()
    try:        
        response = pipeline.predict(building)
        return [round(response[0],2)]
    except ValueError as e:
        raise HTTPException(status_code=400, detail=e)
