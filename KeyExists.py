# Ask the user to input a key and check if it exists in the dictionary.
# Create your own dictionary on something that interest you.(I.e., films, music, action figures, hair styles.)

interests = {"movie":"Black Panther: Wakanda Forever","music":"Good Father","action figures":"Iron Man"}

user_input = input("Enter a key: ")
result = interests.get(user_input)
print(result)