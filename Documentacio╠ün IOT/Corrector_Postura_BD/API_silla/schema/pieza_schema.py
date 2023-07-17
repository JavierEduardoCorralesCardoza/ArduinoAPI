from pydantic import BaseModel 
 
class PiezaSchema(BaseModel): 
    Pieza: str 
    Medida_Pieza: int