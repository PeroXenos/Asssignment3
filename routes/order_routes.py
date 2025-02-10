from fastapi import APIRouter
from config.database import db
from models.order import Order
from bson import ObjectId

router = APIRouter()

@router.post("/")
async def create_order(order: Order):
    order_dict = order.dict()
    result = await db.orders.insert_one(order_dict)
    return {"id": str(result.inserted_id)}

@router.get("/{user_id}")
async def get_orders(user_id: str):
    orders = await db.orders.find({"user_id": user_id}).to_list(100)
    return [{"id": str(o["_id"]), **o} for o in orders]
