# Track grocery store inventory

inventory = {
"Apples": 100,
"Bananas": 80,
"Tomatoes": 60
}

print("Bananas in stock:", inventory["Bananas"])

# adds oranges and apples to the inventory.
inventory["Oranges"] = 50
inventory["Apples"] = 120

# removes tomatoes
inventory.pop("Tomatoes")

# prints the keys and values
for product, qty in inventory.items():
    print(f"Product: {product}, Quantity: {qty}")

apples = {"price":5.0, "quantity":120}
bananas = {"price":3.0, "quantity":80}
oranges = {"price":4.0, "quantity": 50}

# dictionaries in a dictionary
inventory = {
"Apples": apples,
"Bananas": bananas,
"Oranges": oranges
}

# prints the price of bananas
print("Price of Bananas:", inventory["Bananas"]["price"])