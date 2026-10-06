Discount_percentage = 5
Tax_percentage = 13

def calculate_item_total(item_name, cart):
    price = cart[item_name]["price"]
    quantity = cart[item_name]["quantity"]

    return price * quantity

def calculate_subtotal(cart):  
    subtotal = 0 
    for item in cart.keys():  #keys vanesi item haru matra aauxa
        item_total = calculate_item_total(item, cart)
        subtotal += item_total    #subtotal 0 xa ani harek item ko price + hudai aauxa jastai first ma subtotal 0 xa ani tespaxi item ko price jodxa + 1 hudai 
    return subtotal

def calculate_discount(cart):
    subtotal = calculate_subtotal(cart)
    discount_amount = subtotal * Discount_percentage/100

    return discount_amount

def calculate_tax(cart):
    amount_after_discount = calculate_subtotal(cart) - calculate_discount(cart)
    tax_amount = amount_after_discount * Tax_percentage/100

    return tax_amount

def calculate_final_amount(cart):
    amount_after_discount = calculate_subtotal(cart) - calculate_discount(cart)
    tax_amount = calculate_tax(cart)

    final_amount = amount_after_discount + tax_amount

    return final_amount

#this is only for heading of bill summary
# ========================================
#              BILL SUMMARY
# ========================================
def show_bill_summary(cart):
    bill_draft = """
        ========================================
        BILL SUMMARY
        ========================================
    """
    for item_key in cart.keys():
        item_summary = f"""
        product : {cart[item_key]["label"]}
        price :Rs. {cart[item_key]["price"]}
        quantity : {cart[item_key]["quantity"]}
        total :Rs. {calculate_item_total(item_key, cart)}
        """
    # print(item_summary)
        bill_draft += item_summary
    # print(bill_draft)

    bill_draft += f"""
        ----------------------------------------
        Subtotal :Rs .{calculate_subtotal(cart)}
        Discount : {calculate_discount(cart)}
        Tax : {calculate_tax(cart)}
        ----------------------------------------
        Final Amount :{calculate_final_amount(cart)}
        ========================================
        """
    print(bill_draft)

