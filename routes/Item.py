from config.db import item_collection
from middleware.user_auth import  get_current_user
from fastapi import APIRouter, Depends, HTTPException
from bson import ObjectId
from models.Item import ItemModel
router = APIRouter()

@router.post("/items/", response_model=ItemModel)
async def create_item(item: ItemModel, current_user: dict = Depends(get_current_user)):
    db_item = item_collection.insert_one({"name": item.name, "description": item.description})
    return {"name": item.name, "description": item.description}

@router.get("/items/", response_model=list[ItemModel])
async def read_items(current_user: dict = Depends(get_current_user)):
    items = list(item_collection.find())
    # Convert ObjectId to string for each item in the response
    for item in items:
        item['_id'] = str(item['_id'])
    return items

@router.get("/delete_items/{item_id}", response_model=dict)
async def delete_item(item_id: str, current_user: dict = Depends(get_current_user)):
    # Check if the item exists
    item = item_collection.find_one({"_id": ObjectId(item_id)})
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    
    # Check if the user has permission to delete the item (you can customize this logic)
    if item.get("owner") != current_user["sub"]:
        raise HTTPException(status_code=403, detail="Permission denied")
    
    # Delete the item
    item_collection.delete_one({"_id": ObjectId(item_id)})
    return {"message": "Item deleted successfully"}

@router.get("/update_items/{item_id}", response_model=dict)
async def update_item(item_id: str, updated_item: ItemModel, current_user: dict = Depends(get_current_user)):
    # Check if the item exists
    existing_item = item_collection.find_one({"_id": ObjectId(item_id)})
    if not existing_item:
        raise HTTPException(status_code=404, detail="Item not found")

    # Check if the user has permission to update the item (you can customize this logic)
    if existing_item.get("owner") != current_user["sub"]:
        raise HTTPException(status_code=403, detail="Permission denied")

    # Update the item
    item_collection.update_one({"_id": ObjectId(item_id)}, {"$set": updated_item.dict()})
    return {"message": "Item updated successfully"}
