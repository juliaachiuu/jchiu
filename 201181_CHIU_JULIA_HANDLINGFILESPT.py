{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "ddef66dd",
   "metadata": {},
   "source": [
    "The old programmers of Coffee Python encoded this data in a dictionary:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9c8916ed",
   "metadata": {},
   "outputs": [],
   "source": [
    "# NON-INTERACTIVE CODE CELL. YOU MAY RUN THIS CELL, BUT DO NOT EDIT IT.\n",
    "# FOR DEMONSTRATION PURPOSES ONLY. DO NOT EDIT.\n",
    "\n",
    "products = {\n",
    "    \"americano\":{\"name\":\"Americano\",\"price\":150.00},\n",
    "    \"brewedcoffee\":{\"name\":\"Brewed Coffee\",\"price\":110.00},\n",
    "    \"cappuccino\":{\"name\":\"Cappuccino\",\"price\":170.00},\n",
    "    \"dalgona\":{\"name\":\"Dalgona\",\"price\":170.00},\n",
    "    \"espresso\":{\"name\":\"Espresso\",\"price\":140.00},\n",
    "    \"frappuccino\":{\"name\":\"Frappuccino\",\"price\":170.00},\n",
    "}"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "730b6431",
   "metadata": {},
   "source": [
    "\n",
    "Problem 1: Product Information Lookup\n",
    "Write a function called get_product that takes one positional argument (str) code that is a product code of one of Coffee Python's products. The function should return the dictionary containing the information about the product whose code was passed to the function.\n",
    "\n",
    "For example,\n",
    "get_product(\"espresso\")\n",
    "\n",
    "should return\n",
    "\n",
    "{\"name\":\"Espresso\",\"price\":140.00}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "807a6b65",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'name': 'Espresso', 'price': 140.0}"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# CODE CELL\n",
    "# PROBLEM 1\n",
    "\n",
    "def get_product(code):\n",
    "    item = products[code]\n",
    "    return item\n",
    "get_product(\"espresso\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "29c8c31e",
   "metadata": {},
   "source": [
    "Problem 2: Product Property Lookup\n",
    "Write a function called get_property that takes two positional arguments: (str) code and (str) property. The function should return the value appropriate property for the product code entered.\n",
    "\n",
    "For example,\n",
    "get_property(\"espresso\", \"price\")\n",
    "\n",
    "should return\n",
    "\n",
    "140.0 or an equivalent float."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "ad2b0180",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "140.0"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# CODE CELL\n",
    "# PROBLEM 2\n",
    "\n",
    "def get_property (code, propertyy):\n",
    "    description = products[code][propertyy]\n",
    "    return description\n",
    "get_property(\"espresso\",\"price\")\n",
    "    "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2dc904ec",
   "metadata": {},
   "source": [
    "Problem 3: The Point-of-Sale Terminal¶\n",
    "Write a function called main that takes no positional arguments. This function should not return anything.\n",
    "\n",
    "When this function is called, it should begin a session. The session should prompt its user, the clerk, to input data about a customer's orders until the clerk enters the string \"/\".\n",
    "\n",
    "Each line of input consists of two elements: the product code and the quantity. Lines of input are formatted as follows: \"{product_code},{quantity}\".\n",
    "\n",
    "It is up to you how you will store data about orders. Please use your functions from Problem 1 and Problem 2 in answering this problem.\n",
    "\n",
    "The function should write a file called receipt.txt that provides a summarized report of the session. The receipt should be formatted as follows:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "1f09cad6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "==\n",
      "CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL\n",
      "{code}\t\t\t{name}\t\t\t{quantity}\t\t\t{subtotal}\n",
      "\n",
      "Total:\t\t\t\t\t\t\t\t\t\t{total}\n",
      "==\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# NON-INTERACTIVE CODE CELL. YOU MAY RUN THIS CELL, BUT DO NOT EDIT IT.\n",
    "# FOR DEMONSTRATION PURPOSES ONLY. DO NOT EDIT.  \n",
    "\n",
    "# ADJUST THE NUMBER OF TABS AS NECESSARY TO FORMAT IT NICELY.\n",
    "print('''\n",
    "==\n",
    "CODE\\t\\t\\tNAME\\t\\t\\tQUANTITY\\t\\t\\tSUBTOTAL\n",
    "{code}\\t\\t\\t{name}\\t\\t\\t{quantity}\\t\\t\\t{subtotal}\n",
    "\n",
    "Total:\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t{total}\n",
    "==\n",
    "''')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "dccb4fa1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "==\n",
      "CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL\n",
      "cappuccino\t\tCappuccino\t\t1\t\t\t\t170.0\n",
      "brewedcoffee\t\tBrewed Coffee\t\t5\t\t\t\t550.0\n",
      "\n",
      "Total:\t\t\t\t\t\t\t\t\t\t720.0\n",
      "==\n",
      "\n"
     ]
    }
   ],
   "source": [
    "# NON-INTERACTIVE CODE CELL. YOU MAY RUN THIS CELL, BUT DO NOT EDIT IT.\n",
    "# FOR DEMONSTRATION PURPOSES ONLY. DO NOT EDIT.  \n",
    "\n",
    "# Example:\n",
    "print('''\n",
    "==\n",
    "CODE\\t\\t\\tNAME\\t\\t\\tQUANTITY\\t\\t\\tSUBTOTAL\n",
    "cappuccino\\t\\tCappuccino\\t\\t1\\t\\t\\t\\t170.0\n",
    "brewedcoffee\\t\\tBrewed Coffee\\t\\t5\\t\\t\\t\\t550.0\n",
    "\n",
    "Total:\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t720.0\n",
    "==\n",
    "''')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4cc5f51d",
   "metadata": {},
   "source": [
    "Specifications:\n",
    "\n",
    "The receipt should provide a summary of all the orders made during the session.\n",
    "A product must only appear if it has been ordered at least once during the session. In other words, if a product is not ordered, then it should not appear in the receipt.\n",
    "A product must appear only once even if it has been ordered multiple times. In other words, if a product is ordered multiple times, then it should only have one entry in the receipt that describes the sum of all of the orders made for that product.\n",
    "Products must appear in alphabetical order."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "925e8be1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Enter order.Include the product and quantityamericano,2\n",
      "==CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL\n",
      "americano\t\t\tAmericano\t\t\t2\t\t\t\t300.0Total:\t\t\t\t\t\t\t\t\t\t300.0==\n",
      "Enter order.Include the product and quantityamericano,1\n",
      "==CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL\n",
      "americano\t\t\tAmericano\t\t\t3\t\t\t\t450.0Total:\t\t\t\t\t\t\t\t\t\t450.0==\n",
      "Enter order.Include the product and quantityamericano,4\n",
      "==CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL\n",
      "americano\t\t\tAmericano\t\t\t7\t\t\t\t1050.0Total:\t\t\t\t\t\t\t\t\t\t1050.0==\n",
      "Enter order.Include the product and quantity/\n"
     ]
    }
   ],
   "source": [
    "# CODE CELL\n",
    "# PROBLEM 3\n",
    "def main():\n",
    "    products = {\n",
    "        \"americano\":{\"name\":\"Americano\",\"price\":150.00},\n",
    "        \"brewedcoffee\":{\"name\":\"Brewed Coffee\",\"price\":110.00},\n",
    "        \"cappuccino\":{\"name\":\"Cappuccino\",\"price\":170.00},\n",
    "        \"dalgona\":{\"name\":\"Dalgona\",\"price\":170.00},\n",
    "        \"espresso\":{\"name\":\"Espresso\",\"price\":140.00},\n",
    "        \"frappuccino\":{\"name\":\"Frappuccino\",\"price\":170.00},\n",
    "    }\n",
    "\n",
    "    orders =[]\n",
    "    while True:\n",
    "        customer_order = input(\"Enter order.Include the product and quantity\")\n",
    "        if customer_order == \"/\":\n",
    "            break\n",
    "        else:\n",
    "            orders.append(customer_order.split(','))\n",
    "        norepeats=[x[0]for x in orders]\n",
    "        norepeats=list(set(norepeats))\n",
    "        norepeats.sort()\n",
    "        final = []\n",
    "        for item in norepeats:\n",
    "            quantity =[item,0]\n",
    "            for y in orders:\n",
    "                if y[0]==item:\n",
    "                    quantity[1]+=int(y[1])\n",
    "            final.append(quantity)\n",
    "        with open(\"receipt.txt\",\"w\")as f:\n",
    "            f.write(\"\"\"==CODE\\t\\t\\tNAME\\t\\t\\tQUANTITY\\t\\t\\tSUBTOTAL\"\"\")\n",
    "            \n",
    "        subtotal=0\n",
    "        for code in final:\n",
    "            grand_total= int(code[1])*get_property(code[0],'price')\n",
    "            subtotal += grand_total\n",
    "            name = get_property(code[0],\"name\")\n",
    "            with open (\"receipt.txt\",\"a\")as f:\n",
    "                f.write('\\n'+f'{code[0]}\\t\\t\\t{name}\\t\\t\\t{code[1]}\\t\\t\\t\\t{grand_total}')\n",
    "        with open(\"receipt.txt\",\"a+\")as f:\n",
    "            f.write(f'''Total:\\t\\t\\t\\t\\t\\t\\t\\t\\t\\t{subtotal}==''')\n",
    "            f.seek(0)\n",
    "            print(f.read())\n",
    "main()\n",
    "           "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e2fbd217",
   "metadata": {},
   "source": [
    "Problem 4: Final Instructions (28 points)\n",
    "Paste the products dictionary and all three of your functions into a regular Python file called [ID_NUM]_[LAST_NAME]_[FIRST_NAME]_HANDLINGFILES.py (e.g., 199999_ILAGAN_JOSERAMON_HANDLINGFILES.py) and call the main() function once at the very bottom of the file.\n",
    "\n",
    "The program should run properly when it is run using the python command.\n",
    "\n",
    "Only Python files will be checked. Jupyter notebooks will not be checked."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "752386df",
   "metadata": {},
   "outputs": [
    {
     "ename": "IndentationError",
     "evalue": "unindent does not match any outer indentation level (<tokenize>, line 6)",
     "output_type": "error",
     "traceback": [
      "\u001b[0;36m  File \u001b[0;32m\"<tokenize>\"\u001b[0;36m, line \u001b[0;32m6\u001b[0m\n\u001b[0;31m    receipt = []\u001b[0m\n\u001b[0m    ^\u001b[0m\n\u001b[0;31mIndentationError\u001b[0m\u001b[0;31m:\u001b[0m unindent does not match any outer indentation level\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7e295943",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
