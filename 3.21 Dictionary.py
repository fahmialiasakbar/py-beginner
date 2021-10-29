# Dictionary can save any types
colors = {
    12 : "Blue",
    13 : "Red",
    "O" : "Orange"
}
print(colors)
print(colors.get(12, "Not Found"))
print(colors.get("O", "Not Found"))
print(colors.get("H", "Not Found"))