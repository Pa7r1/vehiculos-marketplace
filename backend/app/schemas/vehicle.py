from pydantic import BaseModel
from typing import Optional

# Esquema para la creación de un vehículo
class VehicleCreate(BaseModel):
    price: float
    description: str
    state: str  # Ej: 'new', 'used'
    location_lat: float
    location_lng: float

    class Config:
        orm_mode = True  # Permite que se pueda convertir de los modelos SQLAlchemy

# Esquema de respuesta del vehículo
class VehicleResponse(BaseModel):
    id: int
    price: float
    description: str
    state: str
    location_lat: float
    location_lng: float

    class Config:
        orm_mode = True
