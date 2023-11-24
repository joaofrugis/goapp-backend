from fastapi import APIRouter
from app.models.building import Building
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

router = APIRouter()
database_uri = "mongodb+srv://joaofrugis:4293784*Jaum@goappcluster.u5qlawa.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(database_uri, server_api=ServerApi('1'))
db = client['property-valuation']
collection = db['predict-data']

@router.post("/predict")
async def post_predict(building: Building):
    collection.insert_one(building)
    return building
