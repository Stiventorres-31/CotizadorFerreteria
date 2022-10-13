from pydantic import BaseModel #es una forma de modelar los datos o crear tipos de datos
from typing import Optional

class Personas_schema(BaseModel):
    id_persona: Optional[int]
    cedula:Optional[str]
    nombre_1:Optional[str]
    nombre_2: Optional[str]
    apellido_1:Optional[str]
    apellido_2:Optional[str]
    telefono:Optional[str]
    correo:Optional[str]
    departamento:Optional[str]
    ciudad:Optional[str]
    barrio:Optional[str]
    direccion_residencial:Optional[str]
    punto_referencia:Optional[str]
    