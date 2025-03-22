from pydantic import BaseModel
from typing import Optional

# Esquema para la creación de un usuario
class UserCreate(BaseModel):
    email: str
    password: str
    name: Optional[str] = None

    class Config:
        orm_mode = True  # Para permitir la conversión de modelos de SQLAlchemy a Pydantic

# Esquema para el login de un usuario
class UserLogin(BaseModel):
    email: str
    password: str

    class Config:
        orm_mode = True

# Esquema de respuesta del usuario
class UserResponse(BaseModel):
    id: int
    email: str
    name: Optional[str]

    class Config:
        orm_mode = True
