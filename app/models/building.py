from pydantic import BaseModel

class Building(BaseModel):
    area: float
    dormitorios: int
    banheiros: int
    vagas: int