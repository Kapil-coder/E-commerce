from routes import products
from routes import orders


from fastapi import FastAPI

from db.database import productcollection

app = FastAPI()

#Base route
@app.get("/")
def root():
    return {"message": "E-commerce API is live"}



app.include_router(products.router)
app.include_router(orders.router)
    

