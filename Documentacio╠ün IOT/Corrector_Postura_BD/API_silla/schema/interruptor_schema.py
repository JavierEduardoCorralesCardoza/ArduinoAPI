from pydantic import BaseModel 
from typing import Optional 
 
class InterruptorSchema(BaseModel): 
    ID_Interruptor: Optional[int] 
    Modelo_Interruptor: str
    Posicion_Interruptor: int
