from fastapi import APIRouter, HTTPException
from config.database import db
from models.product import Product
from bson import ObjectId

router = APIRouter()

@router.post("/")
async def create_product(product: Product):
    product_dict = product.dict()
    result = await db.products.insert_one(product_dict)
    return {"id": str(result.inserted_id)}

@router.get("/")
async def get_products():
    products = await db.products.find().to_list(100)
    return [{"id": str(p["_id"]), **p} for p in products]

@router.put("/{product_id}")
async def update_product(product_id: str, product: Product):
    result = await db.products.update_one({"_id": ObjectId(product_id)}, {"$set": product.dict()})
    if result.modified_count:
        return {"message": "Product updated"}
    raise HTTPException(status_code=404, detail="Product not found")
