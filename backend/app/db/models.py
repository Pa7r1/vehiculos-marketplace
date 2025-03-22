from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from backend.app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password_hash = Column(String)
    name = Column(String)
    created_at = Column(DateTime, default=func.now())

    # Relacion con los vehiculos publicados por el usuario
    vehicles = relationship("Vehicle", back_populates="owner")

class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    price = Column(Float, nullable=False)
    description = Column(String, nullable=False)
    state = Column(String, nullable=False)  # 'new', 'used', etc.
    location_lat = Column(Float, nullable=False)
    location_lng = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=func.now())

    # Relacion con el usuario (vendedor)
    owner = relationship("User", back_populates="vehicles")

    # Relacion con las imagenes del vehículo
    images = relationship("VehicleImage", back_populates="vehicle")

    # Relacion con las transacciones
    transactions = relationship("Transaction", back_populates="vehicle")


class VehicleImage(Base):
    __tablename__ = "vehicle_images"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    image_url = Column(String, nullable=False)

    # Relacion con el vehiculo
    vehicle = relationship("Vehicle", back_populates="images")

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(Integer, primary_key=True, index=True)
    buyer_id = Column(Integer, ForeignKey("users.id"))
    seller_id = Column(Integer, ForeignKey("users.id"))
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    price = Column(Float, nullable=False)
    transaction_date = Column(DateTime, default=func.now())

    # Relacion con el comprador, vendedor y vehiculo
    buyer = relationship("User", foreign_keys=[buyer_id])
    seller = relationship("User", foreign_keys=[seller_id])
    vehicle = relationship("Vehicle", back_populates="transactions")
