from cart import calculate_total

def test_calculate_total():
    items = [
        {"price": 100, "quantity": 2}
    ]
    assert calculate_total(items) == 200

def test_discount():
    items = [
        {"price": 100, "quantity": 2}
    ]
    assert calculate_total(items, 10) == 180
