
price_1 = input("What is the price of product 1? ")
quantity_1 = input("What will be the quantity of the product 1? ")
price_2 = input("What is the price of product 2? ")
quantity_2 = input("What will be the quantity of the product 2? ")
price_3 = input("What is the price of product 3? ")
quantity_3 = input("What will be the quantity of the product 3? ")

result_1 = float(price_1) * float(quantity_1)
result_2 = float(price_2) * float(quantity_2)
result_3 = float(price_3) * float(quantity_3)
result_all = result_1 + result_2 + result_3
print("So, that would be " + str(result_all))