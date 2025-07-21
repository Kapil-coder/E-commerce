from fastapi import APIRouter
from models.schemas import Product
from db.database import productcollection

router = APIRouter()


@router.post("/products", status_code=201)
def createprodcut(product:Product):
    # Convert Pydantic model to dictionary

    product_dict= product.model_dump()
    #insert product
    result= productcollection.insert_one(product_dict)

    # Add the DB id to the product dictionary 
    product_dict["_id"]= str(result.inserted_id) 
    return product_dict

@router.get("/products", status_code=200)
def getproducts(name: str = None, size: str = None): # type: ignore
    query = {}

    if name:
        query["name"] = {"$regex": name, "$options": "i"}

    if size:
        query["sizes.size"] = size

    products_cur = productcollection.find(query)  

    products = []
    for product in products_cur:  
        product["_id"] = str(product["_id"])
        products.append(product)

    return products

         