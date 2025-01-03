from fastapi import FastAPI
from pydantic import BaseModel
from app.services.fuzzy_logic import calculate_discount

app = FastAPI()

class DiscountRequest(BaseModel):
    sold: int
    loyalty: int

@app.get("/")
def read_root():
    return {"message": "Welcome to the Fuzzy Discount API"}

@app.post("/calculate_discount")
def get_discount(request: DiscountRequest):
    discount = calculate_discount(request.sold, request.loyalty)
    return {"sold": request.sold, "loyalty": request.loyalty, "discount": discount}
