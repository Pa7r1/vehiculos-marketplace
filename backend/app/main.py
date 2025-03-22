from fastapi import FastAPI
from backend.app.api.v1.endpoints import auth, users, vehicles
from backend.app.db.session import create_db

app = FastAPI()

# Crear las tablas en la base de datos al iniciar el servidor
create_db()

# Registrar las rutas
app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(vehicles.router, prefix="/vehicles", tags=["vehicles"])
