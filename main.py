from fastapi import FastAPI
from routes.product_routes import router as product_router
from routes.user_routes import router as user_router
from routes.order_routes import router as order_router

app = FastAPI()

app.include_router(product_router, prefix="/api/products", tags=["Products"])
app.include_router(user_router, prefix="/api/users", tags=["Users"])
app.include_router(order_router, prefix="/api/orders", tags=["Orders"])

@app.get("/")
async def root():
    return {"message": "E-commerce API is running"}
