from pydantic import BaseModel

class ItemModel(BaseModel):
    name: str
    description: str
