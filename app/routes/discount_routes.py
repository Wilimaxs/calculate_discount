from fastapi import APIRouter
from app.services.fuzzy_logic import calculate_discount

router = APIRouter()

@router.post("/calculate_discount/")
def get_discount(sold_product: int, loyalty: int):
    if sold_product < 0 or loyalty < 0 or loyalty > 100:
        return {"error": "Invalid input. Sold product and loyalty must be within valid ranges."}
    discount = calculate_discount(sold_product, loyalty)
    return {"sold_product": sold_product, "loyalty": loyalty, "discount": discount}
