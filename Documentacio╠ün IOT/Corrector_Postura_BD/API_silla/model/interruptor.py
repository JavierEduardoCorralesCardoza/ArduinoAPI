from sqlalchemy import Table, Column 
from sqlalchemy.sql.sqltypes import Integer, String 
from config.db import engine, metadata 

interruptor = Table( "interruptor", metadata,  
        Column("ID_Interruptor", Integer, primary_key = True), 
        Column("Modelo_Interruptor", String(255), nullable = False), 
        Column("Posicion_Interruptor", Integer, nullable = False), 
)

metadata.create_all(engine)