from backend.app.db.session import SessionLocal
from backend.app.db.models import User
from backend.app.schemas.user import UserCreate  # CORRECCIÓN
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Lógica para crear un usuario
def create_user(user_create: UserCreate):
    db = SessionLocal()
    db_user = db.query(User).filter(User.email == user_create.email).first()
    if db_user:
        raise Exception("User already exists")
    new_user = User(email=user_create.email, password_hash=pwd_context.hash(user_create.password), name=user_create.name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
