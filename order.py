from menu import menu


def get_order():
    while True:
        code = input("Enter item code: ").upper()
        if code in menu:
            break
        print("Invalid code.")

    while True:
        try:
            quantity = int(input("Enter quantity: "))
            if quantity > 0:
                break
            print("Quantity must be more than 0.")
        except ValueError:
            print("Enter a whole number.")

    name = menu[code]["name"]
    price = menu[code]["price"]
    return {"name": name, "price": price, "quantity": quantity}