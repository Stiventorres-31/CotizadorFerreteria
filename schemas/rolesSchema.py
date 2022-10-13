from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class roles_schema(BaseModel):
    id_rol:Optional[int]
    descripcion:Optional[str]
    estado:Optional[int]
    fecha_registro:Optional[datetime]
    fecha_actualizacion:Optional[datetime]
    fecha_cambio_estado:Optional[datetime]