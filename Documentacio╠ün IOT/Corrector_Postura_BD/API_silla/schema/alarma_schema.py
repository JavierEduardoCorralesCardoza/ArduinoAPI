from pydantic import BaseModel 
from typing import Optional 
 
class AlarmaSchema(BaseModel): 
    ID_Alarma: Optional[int] 
    Modelo_Alarma: str
    Posicion_Alarma: int
