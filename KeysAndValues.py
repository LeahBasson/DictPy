# Loop through the Food Type dictionary and print each key with its value.

info = {}

for eachPass in range(3):
    user_input = input("Enter a key-value pair (e.g.fruit:apple): ")
    
    if ":" in user_input:
        key, value = user_input.split(":", 1)
        info[key.strip()] = value.strip()
    
print(info)

for key in info:
    print(key, info[key])