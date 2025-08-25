dict = {}

key = input("Enter key: ")

while (key != "stop"):
    value = int(input("Enter value: "))
    dict[key] = value
    key = input("Enter key: ")

# a dictionary of number values.
print(dict)