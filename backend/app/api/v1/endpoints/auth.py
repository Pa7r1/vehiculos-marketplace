from fastapi import APIRouter, Depends, HTTPException
from backend.app.services.auth_service import authenticate_user, create_access_token
from backend.app.schemas import Token, UserLogin

router = APIRouter()

@router.post("/login", response_model=Token)
def login(user_login: UserLogin):
    user = authenticate_user(user_login.email, user_login.password)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    access_token = create_access_token(user.id)
    return {"access_token": access_token, "token_type": "bearer"}
