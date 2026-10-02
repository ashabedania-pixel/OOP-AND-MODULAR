def show_receipt(orders):
    subtotal = 0
    print("\nRECEIPT")
    for o in orders:
        total = o["price"] * o["quantity"]
        subtotal += total
        print(o["name"], o["quantity"], "x", o["price"], "=", total)

    if subtotal >= 1000:
        discount = subtotal * 0.10
    elif subtotal >= 500:
        discount = subtotal * 0.05
    else:
        discount = 0

    print("Subtotal:", subtotal)
    print("Discount:", discount)
    print("Total:", subtotal - discount)