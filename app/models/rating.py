from pydantic import BaseModel

class Rating(BaseModel):
    predict_data_id: str
    rating: str