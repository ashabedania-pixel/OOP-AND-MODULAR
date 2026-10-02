class Order:

    def __init__(self):
        self.menu = {
            "B1": {"name": "Bacon Cheeseburger", "price": 129},
            "B2": {"name": "Double Beef Burger", "price": 159},
            "F1": {"name": "Crispy French Fries", "price": 69},
            "D1": {"name": "Cola Soft Drink", "price": 49},
        }
        self.items = []

    def show_menu(self):
        print("\nMENU")
        for code, item in self.menu.items():
            print(code, item["name"], "P" + str(item["price"]))

    def add_item(self):
        while True:
            code = input("Enter item code: ").upper()
            if code in self.menu:
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

        name = self.menu[code]["name"]
        price = self.menu[code]["price"]
        self.items.append({"name": name, "price": price, "quantity": quantity})

    def show_receipt(self):
        subtotal = 0
        print("\nRECEIPT")
        for i in self.items:
            total = i["price"] * i["quantity"]
            subtotal += total
            print(i["name"], i["quantity"], "x", i["price"], "=", total)

        if subtotal >= 1000:
            discount = subtotal * 0.10
        elif subtotal >= 500:
            discount = subtotal * 0.05
        else:
            discount = 0

        print("Subtotal:", subtotal)
        print("Discount:", discount)
        print("Total:", subtotal - discount)