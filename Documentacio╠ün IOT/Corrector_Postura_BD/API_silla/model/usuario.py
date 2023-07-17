from sqlalchemy import Table, Column 
from sqlalchemy.sql.sqltypes import Integer, String 
from config.db import engine, metadata 
 
usuario = Table( "usuario", metadata,  
        Column("ID_Usuario", Integer, primary_key = True), 
        Column("Nombre", String(255), nullable = False), 
        Column("Contraseña", String(255), nullable = False), 
        Column("Edad", Integer, nullable = False),
        Column("Genero", String(255), nullable = False)
) 
 
metadata.create_all(engine) 