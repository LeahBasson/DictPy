# Create a dictionary with 3 key-value pairs (name, age, and city)
# Only print the person's name from the dictionary.
# Add a key "email" with a value to the dictionary. Print.
# Change the person's age to 30. Print.
# Remove the "city" key from the dictionary. Print.
# Check if the key "email" exists in the dictionary. Print the email address.
# Print all keys and values in the dictionary. Use a for loop.

info = {"Name":"Leah","Age":20,"City":"Cape Town"}

# access a value
print(info["Name"])

# add a value
info["Email"] = "leahbasson@gmail.com"
print(info)

# change a value
info["Age"] = 21
print(info)

# remove a city
info.pop("City")
print(info)

# check if the key exists
print(info.get("Email"))

# Print all keys and values in the dictionary. Use a for loop.
for key in info:
    print(key, info[key])



