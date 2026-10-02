menu = {
    "B1": {"name": "Bacon Cheeseburger", "price": 129},
    "B2": {"name": "Double Beef Burger", "price": 159},
    "F1": {"name": "Crispy French Fries", "price": 69},
    "D1": {"name": "Cola Soft Drink", "price": 49},
}


def show_menu():
    print("\nMENU")
    for code, item in menu.items():
        print(code, item["name"], "P" + str(item["price"]))