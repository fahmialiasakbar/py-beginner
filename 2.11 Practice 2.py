name_1 = input("What is your name ? ")
name_2 = input("What is your name ? ")
name_3 = input("What is your name ? ")

slices = input("How many slice in the pizza ? ") #for the win

price = input("How much price of the pizza ? ")

slice_1 = input(name_1 + ", how much slice ? ")
slice_2 = input(name_2 + ", how much slice ? ")
slice_3 = input(name_3 + ", how much slice ? ")

pct_1 = float(slice_1)/float(slices)*100
pct_2 = float(slice_2)/float(slices)*100
pct_3 = float(slice_3)/float(slices)*100

pay_1 = pct_1/100*float(price)
pay_2 = pct_2/100*float(price)
pay_3 = pct_3/100*float(price)

print(name_1 + ", you ate " + str(pct_1) + " and should pay " + str(pay_1))
print(name_2 + ", you ate " + str(pct_2) + " and should pay " + str(pay_2))
print(name_3 + ", you ate " + str(pct_3) + " and should pay " + str(pay_3))

