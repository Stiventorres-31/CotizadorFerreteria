from datetime import datetime
from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String
from config.db import meta,engine

fecha=datetime.now()
rolesTable = Table(
    'roles',
    meta,
    Column('id_rol',Integer, primary_key=True),
    Column('descripcion',String(20)),
    Column('estado',Integer,nullable=False),
    Column('fecha_registro',String(50)),
    Column('fecha_actualizacion',String(50)),
    Column('fecha_cambio_estado',String(50))
)
meta.create_all(engine)