def calculate_tax():
    price = 200
    rate = 6.875
    tax = price * rate / 100
    return tax
item = "suit"
price = 200
tax = calculate_tax()
print("A " + item + " costs " + str(price) + " dollars before tax and " + str(tax + price) + " dollars after tax.")