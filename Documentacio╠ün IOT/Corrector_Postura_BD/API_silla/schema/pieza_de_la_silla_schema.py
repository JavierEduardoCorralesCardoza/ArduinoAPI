from pydantic import BaseModel
from typing import Optional 

class Pieza_De_La_SillaSchema(BaseModel):
    ID_Silla_Pieza: Optional[int]
    ID_Silla: int
    Pieza: str