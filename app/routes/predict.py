from fastapi import APIRouter
from app.models.building import Building

router = APIRouter()

@router.post("/predict")
async def post_predict(building: Building):
    return building
