from backend.app.db.session import SessionLocal
from backend.app.db.models import Vehicle
from backend.app.schemas.vehicle import VehicleCreate  # CORRECCIÓN

# Lógica para crear un vehículo
def create_vehicle(vehicle_create: VehicleCreate):
    db = SessionLocal()
    new_vehicle = Vehicle(
        price=vehicle_create.price,
        description=vehicle_create.description,
        state=vehicle_create.state,
        location_lat=vehicle_create.location_lat,
        location_lng=vehicle_create.location_lng
    )
    db.add(new_vehicle)
    db.commit()
    db.refresh(new_vehicle)
    return new_vehicle
