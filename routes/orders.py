from fastapi import APIRouter
from models.schemas import Order
from db.database import ordercollection
from datetime import datetime, timezone

router=APIRouter()

@router.post("/orders",status_code=201)
def createorders(order:Order):
    # Convert Pydantic model to dictionary
    orderdata= order.model_dump()
    orderdata["created_at"]= datetime.now(timezone.utc)
    
      # Insert into MongoDB
    result=ordercollection.insert_one(orderdata)
    return {"id": str(result.inserted_id)}

  



@router.get("/orders/{user_id}",status_code=200)
def getorders(user_id:str,limit:int=10,offset:int=10):
    # filters
    query={"user_id":user_id}

     # offset and limit for pagination
    matching =ordercollection.find(query).skip(offset).limit(limit)

    #  ObjectIds to strings for each order
    orders=[]
    for order in matching:
        order["_id"]=str(order["_id"])
        orders.append(order)

    return orders    
