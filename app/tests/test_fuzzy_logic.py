from app.services.fuzzy_logic import calculate_discount

def test_calculate_discount():
    assert calculate_discount(10, 10) == 0
    assert calculate_discount(50, 50) > 0
    assert calculate_discount(100, 100) == 90
