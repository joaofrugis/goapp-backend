from pydantic import BaseModel

class Building(BaseModel):
    name: str
    value: float