from order import Order

order1 = Order()
order1.show_menu()

while True:
    order1.add_item()
    again = input("Order another item? (yes/no): ").lower()
    if again != "yes":
        break

order1.show_receipt()