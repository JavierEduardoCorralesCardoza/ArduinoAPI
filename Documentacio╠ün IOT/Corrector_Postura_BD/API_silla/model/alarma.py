from sqlalchemy import Table, Column 
from sqlalchemy.sql.sqltypes import Integer, String 
from config.db import engine, metadata 

alarma = Table( "alarma", metadata,  
        Column("ID_Alarma", Integer, primary_key = True), 
        Column("Modelo_Alarma", String(255), nullable = False), 
        Column("Posicion_Alarma", Integer, nullable = False), 
)

metadata.create_all(engine) 