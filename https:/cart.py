def calculate_total(items, discount=0):
    subtotal = sum(
        item["price"] * item["quantity"]
        for item in items
    )

    if discount < 0 or discount > 100:
        raise ValueError("Invalid discount")

    return round(subtotal * (1 - discount / 100), 2)
