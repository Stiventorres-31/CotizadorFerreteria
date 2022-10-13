from fastapi import APIRouter
from config.db import conn
from models.personasModel import personasTable
from schemas.personasSchema import Personas_schema

personasApiRouter = APIRouter()


@personasApiRouter.get("/",response_model=list[Personas_schema])
def get_personas():
    return conn.execute(personasTable.select()).fetchall()


@personasApiRouter.post("/Crear_personas")
def create_personas(personasVariable: Personas_schema):
    new_persona = {
        "cedula": personasVariable.cedula,
        "nombre_1": personasVariable.nombre_1,
        "nombre_2": personasVariable.nombre_2,
        "apellido_1": personasVariable.apellido_1,
        "apellido_2": personasVariable.apellido_2,
        "telefono": personasVariable.telefono,
        "correo": personasVariable.correo,
        "departamento": personasVariable.departamento,
        "ciudad": personasVariable.ciudad,
        "barrio": personasVariable.barrio,
        "direccion_residencial": personasVariable.direccion_residencial,
        "punto_referencia": personasVariable.punto_referencia,
    }
    result = conn.execute(personasTable.insert(), new_persona)
    return conn.execute(
        personasTable.select().where(personasTable.c.id_persona == result.lastrowid)
    ).first()


@personasApiRouter.get("/Buscar_persona/{id_persona}")
def get_persona(id_persona: int):

    return conn.execute(
        personasTable.select().where(personasTable.c.id_persona == id_persona)
    ).first()


@personasApiRouter.delete("/Eliminar_persona/{id_persona}")
def delete_persona(id_persona: int):
    result = conn.execute(
        personasTable.delete().where(personasTable.c.id_persona == id_persona)
    )
    return "Eliminado"


@personasApiRouter.put("/Actualizar_persona/{id_persona}")
def update_persona(id_persona: int, datos: Personas_schema):
    result = conn.execute(personasTable.update().values(
        nombre_1=datos.nombre_1).where(personasTable.c.id_persona == id_persona))
    return "Actualizado"
