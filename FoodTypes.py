# Ask the user to enter 3 key-value pairs (like "fruit: apple"), and store them in a dictionary.
# Print the dictionary.

food = {}

for eachPass in range(3):
    user_input = input("Enter a key-value pair (e.g.fruit:apple): ")
    
    if ":" in user_input:
        key, value = user_input.split(":", 1)
        food[key.strip()] = value.strip()
    
print(food)