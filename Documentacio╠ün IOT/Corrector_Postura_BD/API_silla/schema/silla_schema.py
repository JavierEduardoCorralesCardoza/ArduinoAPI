from pydantic import BaseModel 
from typing import Optional 
 
class SillaSchema(BaseModel): 
    ID_Silla: Optional[int] 
    ID_Usuario: int
    ID_Alarma: int
    ID_Interruptor: int