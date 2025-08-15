# Track player scores.
# Remove "Michael".
# Remove last item.
# Loop through players.

scores = {"Daniel": 15,"Faithlyn": 20,"Abigail": 18,"Michael": 25}

# removes key & attribute
scores.pop("Michael")
print(scores)

# removes last item
scores.popitem()
print(scores)

for x in scores:
    print(f"{x}:", scores[x])