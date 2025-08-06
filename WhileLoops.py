# Keep asking the user for key-value pairs until they type "stop" as the key.

user_input = input("Enter a key-value pair (e.g.fruit:apple) or stop: ")
pairs = {}

while user_input != "stop":
    
    if ":" in user_input:
        key, value = user_input.split(":", 1)
        pairs[key.strip()] = value.strip()
        
    user_input = input("Enter a key-value pair (e.g.fruit:apple) or stop: ")

print(pairs)