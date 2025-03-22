from backend.app.db.session import SessionLocal
from backend.app.db.models import User
from backend.app.schemas.user import UserLogin  # CORRECCIÓN
from backend.app.core.security import create_access_token
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Lógica para autenticar al usuario
def authenticate_user(email: str, password: str):
    db = SessionLocal()
    user = db.query(User).filter(User.email == email).first()
    if user and pwd_context.verify(password, user.password_hash):
        return user
    return None

# Función para crear el JWT
def create_access_token(user_id: int):
    return create_access_token(data={"sub": str(user_id)})
