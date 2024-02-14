from config.db import users_collection
from middleware.user_auth import create_jwt_token, get_current_user
from models.User import UserModel
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from passlib.context import CryptContext
from dotenv import load_dotenv
load_dotenv()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


router = APIRouter()


@router.post("/register/", response_model=dict)
async def register_user(user: UserModel):
    hashed_password = pwd_context.hash(user.password)
    existing_user = users_collection.find_one({"username": user.username})
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered",
        )
    new_user = {"username": user.username, "password": hashed_password}
    users_collection.insert_one(new_user)
    return {"message": "User registered successfully"}


@router.post("/token/", response_model=dict)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = users_collection.find_one({"username": form_data.username})
    if not user or not pwd_context.verify(form_data.password, user["password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    token_data = {"sub": form_data.username}
    access_token = create_jwt_token(token_data)
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/protected/", response_model=dict)
async def protected_route(current_user: dict = Depends(get_current_user)):
    return {"message": "This route is protected", "username": current_user["sub"]}
