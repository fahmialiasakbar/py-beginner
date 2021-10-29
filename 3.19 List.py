variable_1 = "apple"
list_1 = ["apple","banana","ananas","melon","orange"]
print(variable_1)
print(list_1)
list_1[2] = "avocado"
print(list_1)
print(list_1[1:3])
print(list_1[2:])

food = ["hamburger", "pizza", "juice", "fries", "sushi"]
snack = ["pringles", "hotdog", "pizza"]
food.insert(2,"spaghetti")
print(food)
food.extend(snack)
print(food)
print(food.index("pizza"))
print(food.count("pizza"))
drink = ["water", "pepsi"]
random = food.copy() + drink.copy()
food.clear()
print(food)
print(random)
