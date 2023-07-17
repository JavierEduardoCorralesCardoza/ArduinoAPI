from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String 
from config.db import engine, metadata 

sensor_de_la_pieza = Table( "sensor_de_la_pieza", metadata,  
        Column("ID_Pieza_Sensor", Integer, primary_key = True), 
        Column("Pieza", String(255), ForeignKey("pieza.Pieza"), nullable = False), 
        Column("ID_Sensor", Integer, ForeignKey("sensor.ID_Sensor"), nullable = False), 
)

metadata.create_all(engine)