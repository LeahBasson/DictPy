# Count how many values in a dictionary are numbers using a for loop and if.

data = {"a":5,"b":"hello","c":12,"d":"True","e":7}

cnt = 0

for key in data:
    if type(data[key]) == int:
        cnt = cnt + 1
    
print("amount of numbers:",cnt)