from pydantic import BaseModel
from typing import Optional 
from datetime import datetime
 
class MedicionSchema(BaseModel): 

    FechaYHora: datetime
    ID_Pieza_Sensor: int
    Distancia: Optional[int]
