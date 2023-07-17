from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer
from config.db import engine, metadata

silla = Table( "silla", metadata,  
        Column("ID_Silla", Integer, primary_key = True),
        Column("ID_Usuario", Integer, ForeignKey("usuario.ID_Usuario")),
        Column("ID_Alarma", Integer, ForeignKey("alarma.ID_Alarma")),
        Column("ID_Interruptor", Integer, ForeignKey("interruptor.ID_Interruptor"))
)

metadata.create_all(engine)