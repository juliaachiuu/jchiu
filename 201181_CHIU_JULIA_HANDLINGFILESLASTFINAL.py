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
            orders.append(customer_order.split(','))
        norepeats=[x[0]for x in orders]
        norepeats=list(set(norepeats))
        norepeats.sort()
        final = []
        for item in norepeats:
            quantity =[item,0]
            for y in orders:
                if y[0]==item:
                    quantity[1]+=int(y[1])
            final.append(quantity)
        with open("receipt.txt","w")as f:
            f.write("""==CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL""")
            
        subtotal=0
        for code in final:
            grand_total= int(code[1])*get_property(code[0],'price')
            subtotal += grand_total
            name = get_property(code[0],"name")
            with open ("receipt.txt","a")as f:
                f.write('\n'+f'{code[0]}\t\t\t{name}\t\t\t{code[1]}\t\t\t\t{grand_total}')
        with open("receipt.txt","a+")as f:
            f.write(f'''Total:\t\t\t\t\t\t\t\t\t\t{subtotal}==''')
            f.seek(0)
            print(f.read())
main()
           