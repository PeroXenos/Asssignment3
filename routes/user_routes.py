from fastapi import APIRouter, HTTPException
from config.database import db
from models.user import User
from passlib.hash import bcrypt
from bson import ObjectId

router = APIRouter()

@router.post("/register")
async def register_user(user: User):
    user_dict = user.dict()
    user_dict["password"] = bcrypt.hash(user.password)
    result = await db.users.insert_one(user_dict)
    return {"id": str(result.inserted_id)}

@router.post("/login")
async def login_user(email: str, password: str):
    user = await db.users.find_one({"email": email})
    if user and bcrypt.verify(password, user["password"]):
        return {"message": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
