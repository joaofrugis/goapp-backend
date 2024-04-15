from fastapi import APIRouter, HTTPException
import pymongo.server_api
from app.models.building import Building
from app.iamodels.pipeline import Pipeline
import pymongo
from typing import List

router = APIRouter()
uri = "mongodb+srv://joaofrugis:4293784@goappcluster.u5qlawa.mongodb.net/?retryWrites=true&w=majority&appName=GoAPPCluster"
client = pymongo.MongoClient(uri, server_api=pymongo.server_api.ServerApi('1'))
database = client["property-valuation"]
predict_data = database["predict-data"]

@router.post("/predict")
async def post_predict(building: Building):
    pipeline = Pipeline()
    try:
        response = round(pipeline.predict(building)[0],2)
        building_dict = building.model_dump()
        building_dict['result'] = response
        _id = predict_data.insert_one(building_dict)
        return dict({"result": response,"_id": str(_id.inserted_id)})
    except ValueError as e:
        return e