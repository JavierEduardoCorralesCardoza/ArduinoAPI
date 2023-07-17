from pydantic import BaseModel 
from typing import Optional 
 
class UsuarioSchema(BaseModel): 
    ID_Usuario: Optional[int] 
    Nombre: str
    Contraseña: str
    Edad: int
    Genero: str
