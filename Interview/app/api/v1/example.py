from fastapi import APIRouter, HTTPException
from app.schemas.example import ExampleCreate, ExampleResponse

router = APIRouter()

# Simple in-memory storage
data = []

@router.get("/", response_model=list[ExampleResponse])
def list_items():
    return data

@router.post("/", response_model=ExampleResponse, status_code=201)
def create_item(item: ExampleCreate):
    if not item.name:
        raise HTTPException(status_code=400, detail="Name is required")
    new_item = {"id": len(data) + 1, "name": item.name}
    data.append(new_item)
    return new_item
