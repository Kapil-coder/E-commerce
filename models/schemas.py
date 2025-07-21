from pydantic import BaseModel
from typing import List

class SizeOption(BaseModel):
    size: str
    quantity: int

class Product(BaseModel):
    name:str
    price:float
    sizes:List[SizeOption]


class Order(BaseModel):
    user_id: str
    product_ids: List[str]    