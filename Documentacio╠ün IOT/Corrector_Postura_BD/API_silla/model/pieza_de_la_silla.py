from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, metadata

pieza_de_la_silla = Table( "pieza_de_la_silla", metadata,  
        Column("ID_Silla_Pieza", Integer, primary_key = True),
        Column("ID_Silla", Integer, ForeignKey("silla.ID_Silla"), nullable = False),
        Column("Pieza", String(255), ForeignKey("pieza.Pieza"), nullable = False),
)

metadata.create_all(engine)