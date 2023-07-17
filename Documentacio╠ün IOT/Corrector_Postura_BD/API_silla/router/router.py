from fastapi import APIRouter, Response
from fastapi.responses import HTMLResponse, FileResponse
from schema.usuario_schema import UsuarioSchema
from schema.alarma_schema import AlarmaSchema
from schema.silla_schema import SillaSchema
from schema.interruptor_schema import InterruptorSchema
from schema.pieza_schema import PiezaSchema
from schema.sensor_schema import SensorSchema
from schema.pieza_de_la_silla_schema import Pieza_De_La_SillaSchema
from schema.sensor_de_la_pieza_schema import Sensor_De_La_PiezaSchema
from schema.medicion_schema import MedicionSchema
from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT
from config.db import engine
from model.usuario import usuario
from model.alarma import alarma
from model.silla import silla
from model.interruptor import interruptor
from model.pieza import pieza
from model.sensor import sensor
from model.pieza_de_la_silla import pieza_de_la_silla
from model.sensor_de_la_pieza import sensor_de_la_pieza
from model.medicion import medicion
from werkzeug.security import generate_password_hash, check_password_hash 
from typing import List
from datetime import datetime

user = APIRouter()

@user.get("/", response_class=HTMLResponse)
def root():
    return FileResponse("C:/Users/ecard/OneDrive/Escritorio/Correcor_Postura/index.html", status_code=200)

@user.get("/api/usuario", response_model=List[UsuarioSchema]) 
def get_usuario(): 
    with engine.connect() as conn: 
        result = conn.execute( usuario.select() ).fetchall() 
    return result

@user.get("/api/usuario/{ID_Usuario}", response_model=UsuarioSchema) 
def get_usuario(ID_Usuario: int): 
    with engine.connect() as conn: 
        result = conn.execute( usuario.select().where(usuario.c.ID_Usuario == ID_Usuario)).first() 
        return result 

@user.put("/api/usuario/{ID_Usuario}", response_model=UsuarioSchema) 
def update_usuario(data_update: UsuarioSchema, ID_Usuario: int): 
    with engine.connect() as conn: 
        encrypt_passw = generate_password_hash(data_update.Contraseña, "pbkdf2:sha256:30", 30) 
        conn.execute(usuario.update().values(Nombre=data_update.Nombre,  Contraseña=encrypt_passw, Edad=data_update.Edad, Genero=data_update.Genero).where(usuario.c.ID_Usuario == ID_Usuario)) 
        result = conn.execute(usuario.select().where(usuario.c.ID_Usuario == ID_Usuario)).first() 
        return result

@user.post("/api/usuario") 
def create_usuario(data_usuario: UsuarioSchema): 
    with engine.connect() as conn:
        print(data_usuario) 
        new_usuario = data_usuario.dict()
        new_usuario["Contraseña"] = generate_password_hash(data_usuario.Contraseña, "pbkdf2:sha256:30", 30)
        conn.execute(usuario.insert().values(new_usuario))
        return Response(status_code=HTTP_201_CREATED)

@user.delete("/api/usuario/{ID_Usuario}", status_code = HTTP_204_NO_CONTENT)
def delete_usuario(ID_Usuario: int): 
    with engine.connect() as conn: 
        conn.execute( usuario.delete().where(usuario.c.ID_Usuario == ID_Usuario))
        return Response(status_code = HTTP_204_NO_CONTENT)

@user.get("/api/alarma", response_model=List[AlarmaSchema]) 
def get_alarma(): 
    with engine.connect() as conn:
        result = conn.execute( alarma.select() ).fetchall() 
    return result 

@user.get("/api/alarma/{ID_Alarma}", response_model=AlarmaSchema) 
def get_alarma(ID_Alarma: int): 
    with engine.connect() as conn: 
        result = conn.execute( alarma.select().where(alarma.c.ID_Alarma == ID_Alarma)).first() 
        return result 

@user.put("/api/alarma/{ID_Alarma}", response_model=AlarmaSchema) 
def update_alarma(data_update: AlarmaSchema, ID_Alarma: int): 
    with engine.connect() as conn: 
        conn.execute(alarma.update().values(Modelo_Alarma=data_update.Modelo_Alarma, Posicion_Alarma=data_update.Posicion_Alarma).where(alarma.c.ID_Alarma == ID_Alarma)) 
        result = conn.execute(alarma.select().where(alarma.c.ID_Alarma == ID_Alarma)).first() 
        return result

@user.post("/api/alarma") 
def create_alarma(data_alarma: AlarmaSchema): 
    with engine.connect() as conn:
        print(data_alarma) 
        new_alarma = data_alarma.dict()
        conn.execute(alarma.insert().values(new_alarma))
        return Response(status_code=HTTP_201_CREATED)

@user.delete("/api/alarma/{ID_Alarma}", status_code = HTTP_204_NO_CONTENT)
def delete_alarma(ID_Alarma: int): 
    with engine.connect() as conn: 
        conn.execute( alarma.delete().where(alarma.c.ID_Alarma == ID_Alarma))
        return Response(status_code = HTTP_204_NO_CONTENT)

@user.get("/api/interruptor", response_model=List[InterruptorSchema]) 
def get_interruptor(): 
    with engine.connect() as conn:
        result = conn.execute( interruptor.select() ).fetchall() 
    return result 

@user.get("/api/interruptor/{ID_Interruptor}", response_model=InterruptorSchema) 
def get_interruptor(ID_Interruptor: int): 
    with engine.connect() as conn: 
        result = conn.execute( interruptor.select().where(interruptor.c.ID_Interruptor == ID_Interruptor)).first() 
        return result 

@user.put("/api/interruptor/{ID_Interruptor}", response_model=InterruptorSchema) 
def update_interruptor(data_update: InterruptorSchema, ID_Interruptor: int): 
    with engine.connect() as conn: 
        conn.execute(interruptor.update().values(Modelo_interruptor=data_update.Modelo_interruptor, Posicion_interruptor=data_update.Posicion_interruptor).where(interruptor.c.ID_Interruptor == ID_Interruptor)) 
        result = conn.execute(interruptor.select().where(interruptor.c.ID_Interruptor == ID_Interruptor)).first() 
        return result

@user.post("/api/interruptor") 
def create_interruptor(data_interruptor: InterruptorSchema): 
    with engine.connect() as conn:
        print(data_interruptor) 
        new_interruptor = data_interruptor.dict()
        conn.execute(interruptor.insert().values(new_interruptor))
        return Response(status_code=HTTP_201_CREATED)

@user.delete("/api/interruptor/{ID_Interruptor}", status_code = HTTP_204_NO_CONTENT)
def delete_interruptor(ID_Interruptor: int): 
    with engine.connect() as conn: 
        conn.execute( interruptor.delete().where(interruptor.c.ID_Interruptor == ID_Interruptor))
        return Response(status_code = HTTP_204_NO_CONTENT)

@user.get("/api/silla", response_model=List[SillaSchema]) 
def get_silla(): 
    with engine.connect() as conn:
        result = conn.execute( silla.select() ).fetchall() 
    return result 

@user.get("/api/silla/{ID_Silla}", response_model=SillaSchema) 
def get_silla(ID_Silla: int): 
    with engine.connect() as conn: 
        result = conn.execute( silla.select().where(silla.c.ID_Silla == ID_Silla)).first() 
        return result 

@user.put("/api/silla/{ID_Silla}", response_model=SillaSchema) 
def update_silla(data_update: SillaSchema, ID_Silla: int): 
    with engine.connect() as conn: 
        conn.execute(silla.update().values(ID_Usuario=data_update.ID_Usuario, ID_Alarma=data_update.ID_Alarma, ID_Interruptor=data_update.ID_Interruptor).where(silla.c.ID_Silla == ID_Silla)) 
        result = conn.execute(silla.select().where(silla.c.ID_Silla == ID_Silla)).first() 
        return result

@user.post("/api/silla") 
def create_silla(data_silla: SillaSchema): 
    with engine.connect() as conn:
        print(data_silla) 
        new_silla = data_silla.dict()
        conn.execute(silla.insert().values(new_silla))
        return Response(status_code=HTTP_201_CREATED)

@user.delete("/api/silla/{ID_Silla}", status_code = HTTP_204_NO_CONTENT)
def delete_silla(ID_Silla: int): 
    with engine.connect() as conn: 
        conn.execute( silla.delete().where(silla.c.ID_Silla == ID_Silla))
        return Response(status_code = HTTP_204_NO_CONTENT)

@user.get("/api/pieza", response_model=List[PiezaSchema]) 
def get_pieza(): 
    with engine.connect() as conn:
        result = conn.execute( pieza.select() ).fetchall() 
    return result 

@user.get("/api/pieza/{Pieza}", response_model=PiezaSchema) 
def get_pieza(Pieza: str): 
    with engine.connect() as conn: 
        result = conn.execute( pieza.select().where(pieza.c.Pieza == Pieza)).first() 
        return result 

@user.put("/api/pieza/{Pieza}", response_model=PiezaSchema) 
def update_pieza(data_update: PiezaSchema, Pieza: str): 
    with engine.connect() as conn: 
        conn.execute(pieza.update().values(Medida_Pieza=data_update.Medida_Pieza).where(pieza.c.Pieza == Pieza)) 
        result = conn.execute(pieza.select().where(pieza.c.Pieza == Pieza)).first() 
        return result

@user.post("/api/pieza") 
def create_pieza(data_pieza: PiezaSchema): 
    with engine.connect() as conn:
        print(data_pieza) 
        new_pieza = data_pieza.dict()
        conn.execute(pieza.insert().values(new_pieza))
        return Response(status_code=HTTP_201_CREATED)

@user.delete("/api/pieza/{Pieza}", status_code = HTTP_204_NO_CONTENT)
def delete_pieza(Pieza: str): 
    with engine.connect() as conn: 
        conn.execute( pieza.delete().where(pieza.c.Pieza == Pieza))
        return Response(status_code = HTTP_204_NO_CONTENT)

@user.get("/api/sensor", response_model=List[SensorSchema]) 
def get_sensor(): 
    with engine.connect() as conn:
        result = conn.execute( sensor.select() ).fetchall() 
    return result 

@user.get("/api/sensor/{ID_Sensor}", response_model=SensorSchema) 
def get_sensor(ID_Sensor: int): 
    with engine.connect() as conn: 
        result = conn.execute( sensor.select().where(sensor.c.ID_Sensor == ID_Sensor)).first() 
        return result 

@user.put("/api/sensor/{ID_Sensor}", response_model=SensorSchema) 
def update_sensor(data_update: SensorSchema, ID_Sensor: int): 
    with engine.connect() as conn: 
        conn.execute(sensor.update().values(Modelo_Sensor=data_update.Modelo_Sensor).where(sensor.c.ID_Sensor == ID_Sensor)) 
        result = conn.execute(sensor.select().where(sensor.c.ID_Sensor == ID_Sensor)).first() 
        return result

@user.post("/api/sensor") 
def create_sensor(data_sensor: SensorSchema): 
    with engine.connect() as conn:
        print(data_sensor) 
        new_sensor = data_sensor.dict()
        conn.execute(sensor.insert().values(new_sensor))
        return Response(status_code=HTTP_201_CREATED)

@user.delete("/api/sensor/{ID_Sensor}", status_code = HTTP_204_NO_CONTENT)
def delete_sensor(ID_Sensor: int): 
    with engine.connect() as conn: 
        conn.execute( sensor.delete().where(sensor.c.ID_Sensor == ID_Sensor))
        return Response(status_code = HTTP_204_NO_CONTENT)

@user.get("/api/pieza_de_la_silla", response_model=List[Pieza_De_La_SillaSchema]) 
def get_pieza_de_la_silla(): 
    with engine.connect() as conn:
        result = conn.execute( pieza_de_la_silla.select() ).fetchall() 
    return result 

@user.get("/api/pieza_de_la_silla/{ID_Silla_Pieza}", response_model=Pieza_De_La_SillaSchema) 
def get_pieza_de_la_silla(ID_Silla_Pieza: int): 
    with engine.connect() as conn: 
        result = conn.execute( pieza_de_la_silla.select().where(pieza_de_la_silla.c.ID_Silla_Pieza == ID_Silla_Pieza)).first() 
        return result 

@user.put("/api/pieza_de_la_silla/{ID_Silla_Pieza}", response_model=Pieza_De_La_SillaSchema) 
def update_pieza_de_la_silla(data_update: Pieza_De_La_SillaSchema, ID_Silla_Pieza: int): 
    with engine.connect() as conn: 
        conn.execute(pieza_de_la_silla.update().values(ID_Silla=data_update.ID_Silla, Pieza=data_update.Pieza).where(pieza_de_la_silla.c.ID_Silla_Pieza == ID_Silla_Pieza)) 
        result = conn.execute(pieza_de_la_silla.select().where(pieza_de_la_silla.c.ID_Silla_Pieza == ID_Silla_Pieza)).first() 
        return result

@user.post("/api/pieza_de_la_silla") 
def create_pieza_de_la_silla(data_pieza_de_la_silla: Pieza_De_La_SillaSchema): 
    with engine.connect() as conn:
        print(data_pieza_de_la_silla) 
        new_pieza_de_la_silla = data_pieza_de_la_silla.dict()
        conn.execute(pieza_de_la_silla.insert().values(new_pieza_de_la_silla))
        return Response(status_code=HTTP_201_CREATED)

@user.delete("/api/pieza_de_la_silla/{ID_Silla_Pieza}", status_code = HTTP_204_NO_CONTENT)
def delete_pieza_de_la_silla(ID_Silla_Pieza: int): 
    with engine.connect() as conn: 
        conn.execute( pieza_de_la_silla.delete().where(pieza_de_la_silla.c.ID_Silla_Pieza == ID_Silla_Pieza))
        return Response(status_code = HTTP_204_NO_CONTENT)

@user.get("/api/sensor_de_la_pieza", response_model=List[Sensor_De_La_PiezaSchema]) 
def get_sensor_de_la_pieza(): 
    with engine.connect() as conn:
        result = conn.execute( sensor_de_la_pieza.select() ).fetchall() 
    return result 

@user.get("/api/sensor_de_la_pieza/{ID_Pieza_Sensor}", response_model=Sensor_De_La_PiezaSchema) 
def get_sensor_de_la_pieza(ID_Pieza_Sensor: int): 
    with engine.connect() as conn: 
        result = conn.execute( sensor_de_la_pieza.select().where(sensor_de_la_pieza.c.ID_Pieza_Sensor == ID_Pieza_Sensor)).first() 
        return result 

@user.put("/api/sensor_de_la_pieza/{ID_Pieza_Sensor}", response_model=Sensor_De_La_PiezaSchema) 
def update_sensor_de_la_pieza(data_update: Sensor_De_La_PiezaSchema, ID_Pieza_Sensor: int): 
    with engine.connect() as conn: 
        conn.execute(sensor_de_la_pieza.update().values(Pieza=data_update.Pieza, ID_Sensor=data_update.ID_Sensor).where(sensor_de_la_pieza.c.ID_Pieza_Sensor == ID_Pieza_Sensor)) 
        result = conn.execute(sensor_de_la_pieza.select().where(sensor_de_la_pieza.c.ID_Pieza_Sensor == ID_Pieza_Sensor)).first() 
        return result

@user.post("/api/sensor_de_la_pieza") 
def create_sensor_de_la_pieza(data_sensor_de_la_pieza: Sensor_De_La_PiezaSchema): 
    with engine.connect() as conn:
        print(data_sensor_de_la_pieza) 
        new_sensor_de_la_pieza = data_sensor_de_la_pieza.dict()
        conn.execute(sensor_de_la_pieza.insert().values(new_sensor_de_la_pieza))
        return Response(status_code=HTTP_201_CREATED)

@user.delete("/api/sensor_de_la_pieza/{ID_Pieza_Sensor}", status_code = HTTP_204_NO_CONTENT)
def delete_sensor_de_la_pieza(ID_Pieza_Sensor: int): 
    with engine.connect() as conn: 
        conn.execute( sensor_de_la_pieza.delete().where(sensor_de_la_pieza.c.ID_Pieza_Sensor == ID_Pieza_Sensor))
        return Response(status_code = HTTP_204_NO_CONTENT)

@user.get("/api/medicion", response_model=List[MedicionSchema]) 
def get_medicion(): 
    with engine.connect() as conn:
        result = conn.execute( medicion.select() ).fetchall() 
    return result

@user.get("/api/medicion/{FechaYHora}", response_model=MedicionSchema) 
def get_medicion(FechaYHora: datetime): 
    with engine.connect() as conn: 
        result = conn.execute( medicion.select().where(medicion.c.FechaYHora == FechaYHora)).first() 
        return result 

@user.put("/api/medicion/{FechaYHora}", response_model=MedicionSchema) 
def update_medicion(data_update: MedicionSchema, FechaYHora: datetime, ID_Pieza_Sensor: int): 
    with engine.connect() as conn: 
        conn.execute(medicion.update().values(ID_Pieza_Sensor=data_update.ID_Pieza_Sensor, Distancia=data_update.Distancia).where(medicion.c.FechaYHora == FechaYHora and medicion.c.ID_Pieza_Sensor == ID_Pieza_Sensor)) 
        result = conn.execute(medicion.select().where(medicion.c.FechaYHora == FechaYHora)).first() 
        return result

@user.post("/api/medicion") 
def create_medicion(data_medicion: MedicionSchema): 
    with engine.connect() as conn:
        print(data_medicion) 
        new_medicion = data_medicion.dict()
        conn.execute(medicion.insert().values(new_medicion))
        return Response(status_code=HTTP_201_CREATED)

@user.delete("/api/medicion/{FechaYHora}", status_code = HTTP_204_NO_CONTENT)
def delete_medicion(FechaYHora: datetime): 
    with engine.connect() as conn: 
        conn.execute( medicion.delete().where(medicion.c.FechaYHora == FechaYHora))
        return Response(status_code = HTTP_204_NO_CONTENT)

@user.get("/api/postura/{ID_Silla}") 
def get_postura(): 
    with engine.connect() as conn:
        result = conn.execute( medicion.select().where( medicion.c.ID_Pieza_Sensor == sensor_de_la_pieza.c.ID_Pieza_Sensor and sensor_de_la_pieza.c.Pieza == pieza.c.Pieza and pieza.c.Pieza == pieza_de_la_silla.c.Pieza and pieza_de_la_silla.c.ID_Silla == silla.c.ID_Silla and medicion.c.ID_Pieza_Sensor.unique()) ).fetchall()
    return result