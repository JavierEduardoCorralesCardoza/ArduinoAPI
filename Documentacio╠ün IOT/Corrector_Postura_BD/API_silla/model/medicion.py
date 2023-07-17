from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, DateTime
from config.db import engine, metadata 

medicion = Table( "medicion", metadata,  
        Column("FechaYHora", DateTime, primary_key = True), 
        Column("ID_Pieza_Sensor", Integer, ForeignKey("sensor_de_la_pieza.ID_Pieza_Sensor"), primary_key = True), 
        Column("Distancia", Integer, nullable = False)
)

metadata.create_all(engine)