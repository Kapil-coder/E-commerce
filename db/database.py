from pymongo import MongoClient
from dotenv import load_dotenv
client = MongoClient()
import os

load_dotenv()

Url= os.getenv("MONGO_URL")

client = MongoClient(Url)

db=client["hrone"]

productcollection= db["products"]
ordercollection =db["order"]