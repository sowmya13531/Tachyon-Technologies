from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()


#Allow all origins 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Pydantic Model
class Item(BaseModel):
    name: str
    price: float

#GET route
@app.get("/")
def home():
    return {"message": "fastAPI is working"}

#POST route
@app.post("/items")
def create_item(item: Item):
    return{
        "message": "Item received",
        "item": item
    }