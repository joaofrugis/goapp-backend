from fastapi import APIRouter, HTTPException
from app.models.building import Building
from app.models.rating import Rating
from app.iamodels.pipeline import Pipeline
from app.config.database import MongoDBConnection
import logging

router = APIRouter()
pipeline = Pipeline()
connection = MongoDBConnection()
logger = logging.getLogger()

class Predict:
    @router.post("/predict")
    def post_predict(building: Building):
        try:
            response = round(pipeline.predict(building)[0],2)
            building_dict = building.model_dump()
            building_dict['result'] = response
            connection.connect()
            _id = connection.insert_one_data(connection.get_collection('predict-data'), building_dict)
            return dict({"result": response,"_id": str(_id.inserted_id)})
        except Exception as error:
            logger.error(f"Error predicting: {error}")
            raise HTTPException(status_code=400, detail="Bad Request")
        
    
    @router.post('/test')
    def post_test(building: Building):
        return building
    
    @router.post("/predict-rating")
    def post_predict_rating(rating: Rating):
        try:
            rating_dict = rating.model_dump()
            connection.connect()
            connection.insert_one_data(connection.get_collection('predict-rating'), rating_dict)
            return rating
        except Exception as error:
            logger.error(f"Error predicting: {error}")
            raise HTTPException(status_code=400, detail="Bad Request")
