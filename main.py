from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app=FastAPI();

class Item(BaseModel):
    id: int
    name:str
    origin:str

items: List[Item]=[]

@app.get("/")
def read_root():
    return {"message": "Welcome to Taroo"}


@app.get("/items")
def get_items():
    return items

    

# @app.post("/items")
# def app_tea(item:Item):
#     items.append(item)
#     return item

# @app.put("/items/{item_id}")
# def update_item(item_id:int, item:Item):
#     for index, i in items:
#         if i.id==item_id:
#             i.name=item.name
#             i.origin=item.origin
#             return i
#     return {"error":"Item not found"}


# @app.delete("/items/{item_id}")
# def delete_item(item_id:int):
#     for index,i in enumerate(items):
#         if i.id==item_id:
#             deleted=items.pop(index)
#             return  deleted
#     return {"error":"Item not found"}

