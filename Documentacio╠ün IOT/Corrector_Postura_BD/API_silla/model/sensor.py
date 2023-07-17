from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, TIMESTAMP
from config.db import engine, metadata

sensor = Table( "sensor", metadata,  
        Column("ID_Sensor", Integer, primary_key = True),
        Column("Modelo_Sensor", String(255), nullable = False)
)

metadata.create_all(engine)