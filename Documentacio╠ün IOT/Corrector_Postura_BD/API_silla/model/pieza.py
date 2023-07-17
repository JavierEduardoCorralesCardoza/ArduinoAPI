from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, metadata

pieza = Table( "pieza", metadata,  
        Column("Pieza", String(255), primary_key = True),
        Column("Medida_Pieza", Integer, nullable = False)
)

metadata.create_all(engine)