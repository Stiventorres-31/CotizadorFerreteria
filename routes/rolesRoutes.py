from datetime import datetime
from fastapi import APIRouter
from config.db import conn
from models.rolesModel import rolesTable
from schemas.rolesSchema import roles_schema

rolesApiRouter=APIRouter()

@rolesApiRouter.get("/roles",response_model=list[roles_schema])
def get_roles():
    return conn.execute(rolesTable.select()).fetchall()

@rolesApiRouter.post("/crear_rol")
def create_roles(rolesVariable: roles_schema):
    new_rol={
        "descripcion":rolesVariable.descripcion,
        "estado":1,
        "fecha_registro":datetime.now()
    }
    conn.execute(rolesTable.insert(),new_rol)
    return "Rol creado"

@rolesApiRouter.put("/eliminar_rol/{id_rol}")
def delete_roles(id_rol:int, datos: roles_schema):
    conn.execute(rolesTable.update().values(
        estado=datos.estado,
        fecha_cambio_estado=datetime.now()).where(
            rolesTable.c.id_rol == id_rol))
    return "Rol eliminado"

""" def delete_roles(id_rol:int):
    conn.execute(rolesTable.delete().where(rolesTable.c.id_rol==id_rol))
    return "Rol eliminado" """

@rolesApiRouter.put("/actualizar_rol/{id_rol}")
def update_roles(id_rol:int, datos: roles_schema):
    conn.execute(rolesTable.update().values(
        descripcion=datos.descripcion,
        fecha_actualizacion=datetime.now()).where(
            rolesTable.c.id_rol == id_rol))
            
    return "Rol actualizado"