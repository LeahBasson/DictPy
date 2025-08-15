# Store book details in a dictionary
# Print the title and author.
# Get the year using .get().
# Use .get() to check "ISBN" with default "Not Available"

book_details = {"title": "Things Fall Apart","author": "Chinua Achebe","year": 1958,"available": True}

print("title: ",book_details["title"],"\nauthor:",book_details["author"])

year = book_details.get("year")
print(year)

# default is the option if ISBN doesn't exist.
print(book_details.get("ISBN", "Not available"))