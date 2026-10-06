from bill import show_bill_summary
cart = {}
MENU = """
    1.add item to cart
    2.show bill summary
    3.Quit
"""
while True:
    print(MENU)
    user_choice = input("choice >>>")
    if user_choice == "1":
        item_name = input("Item name: ")
        item_price = float(input("Item price: "))
        item_quantity = int(input("Item quantity: "))
        cart[item_name] = {
            "label" : item_name.capitalize(),
            "price" : item_price,
            "quantity" :item_quantity
        }
        
    elif user_choice == "2":
        show_bill_summary(cart)
    elif user_choice == "3":
        break
    else:
        print("invalid choice. choose [1-3]")




