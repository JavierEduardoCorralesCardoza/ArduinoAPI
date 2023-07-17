from pydantic import BaseModel
from typing import Optional 

class Sensor_De_La_PiezaSchema(BaseModel):
    ID_Pieza_Sensor: Optional[int]
    Pieza: str
    ID_Sensor: int