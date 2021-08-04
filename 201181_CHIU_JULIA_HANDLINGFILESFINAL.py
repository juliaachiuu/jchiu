
# NON-INTERACTIVE CODE CELL. YOU MAY RUN THIS CELL, BUT DO NOT EDIT IT.
# FOR DEMONSTRATION PURPOSES ONLY. DO NOT EDIT.

products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}
# CODE CELL
# PROBLEM 1

def get_product(code):
    item = products[code]
    return item
get_product("espresso")
# CODE CELL
# PROBLEM 2

def get_property (code, propertyy):
    description = products[code][propertyy]
    return description
get_property("espresso","price")
    # NON-INTERACTIVE CODE CELL. YOU MAY RUN THIS CELL, BUT DO NOT EDIT IT.
# FOR DEMONSTRATION PURPOSES ONLY. DO NOT EDIT.  

# ADJUST THE NUMBER OF TABS AS NECESSARY TO FORMAT IT NICELY.
print('''
==
CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL
{code}\t\t\t{name}\t\t\t{quantity}\t\t\t{subtotal}

Total:\t\t\t\t\t\t\t\t\t\t{total}
==
''')
# NON-INTERACTIVE CODE CELL. YOU MAY RUN THIS CELL, BUT DO NOT EDIT IT.
# FOR DEMONSTRATION PURPOSES ONLY. DO NOT EDIT.  

# Example:
print('''
==
CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL
cappuccino\t\tCappuccino\t\t1\t\t\t\t170.0
brewedcoffee\t\tBrewed Coffee\t\t5\t\t\t\t550.0

Total:\t\t\t\t\t\t\t\t\t\t720.0
==
''')
# CODE CELL
# PROBLEM 3
def main():
    products = {
        "americano":{"name":"Americano","price":150.00},
        "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
        "cappuccino":{"name":"Cappuccino","price":170.00},
        "dalgona":{"name":"Dalgona","price":170.00},
        "espresso":{"name":"Espresso","price":140.00},
        "frappuccino":{"name":"Frappuccino","price":170.00},
    }

    orders =[]
    while True:
        customer_order = input("Enter order.Include the product and quantity")
        if customer_order == "/":
            break
        else:
            customerorderlist = customer_order.split(",")
            orders.append(customerorderlist)
            print(customerorderlist)
            print(customer_order)

    receipt = []
    receipt.append("CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL\n")
    total = 0
    for order in orders:
    #     print(orders)
        code = order[0]
        name = get_property(order[0],"name")
    #     print(name)
        quantity = order[1]
    #     print(quantity)
        subtotal = float(str(quantity)) * get_property(order[0],"price")
        total = subtotal+total
    #     print(subtotal)
        receipt.append(f"{code}\t\t\t{name}\t\t{quantity}\t\t\t{subtotal}\n")

    receipt.append(f"\nTotal:\t\t\t\t\t\t\t\t\t\t{total}")
    receipt = "".join(receipt)
    # print(receipt)

    with open("receipt.txt","w") as f:
        f.write(receipt)

main()
