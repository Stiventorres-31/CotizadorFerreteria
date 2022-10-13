from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta,engine

personasTable = Table(
    "personas",
    meta,
    Column("id_persona", Integer, primary_key=True),
    Column("cedula", String(15), unique=True,nullable=False),
    Column("nombre_1", String(45), nullable=False),
    Column("nombre_2", String(45), nullable=True),
    Column("apellido_1", String(45), nullable=False),
    Column("apellido_2", String(45), nullable=True),
    Column("telefono", String(10), nullable=True),
    Column("correo", String(100), nullable=True),
    Column("departamento", String(50), nullable=False),
    Column("ciudad", String(45), nullable=False),
    Column("barrio", String(45), nullable=False),
    Column("direccion_residencial", String(200), nullable=False),
    Column("punto_referencia", String(200), nullable=True)
)
meta.create_all(engine)
