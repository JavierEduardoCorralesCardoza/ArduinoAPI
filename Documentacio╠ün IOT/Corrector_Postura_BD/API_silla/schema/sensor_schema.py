from pydantic import BaseModel 
from typing import Optional 
 
class SensorSchema(BaseModel): 
    ID_Sensor: Optional[int] 
    Modelo_Sensor: str