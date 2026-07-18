from pydantic import BaseModel, Field
from typing import List

class DetallesImagenJSON(BaseModel):
    titulo:str = Field(
        description= "Define el título adecuado para la imagen analizada."
    )
    descripcion:str = Field(
        description= "Coloca aquí una descripción detallada del análisis de la imagen."
    )
    etiqueta:List[str] = Field(
        description= "Define 2 palabras-clave para la imagen analizada"
    )