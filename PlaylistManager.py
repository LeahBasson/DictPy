# Build a music playlist manager

# list witin a dictionary.
playlist = {"title": "Chill Beats","genre": "Lo-Fi","songs": ["Dreaming", "Sunset Drive", "Ocean Waves"]}

# display genre
print("Genre:", playlist["genre"],"\n")

# add duration
playlist.update({"duration":45})

# change the title
playlist.update({"title":"Friday Vibes"})

#remove the genre
playlist.pop("genre")

# prints the updated dictionary. 
for key, value in playlist.items():
    print(f"{key}: {value}")
    
# the 1st playlist is the playlist at the start.
# and the 2nd playlist is new one dictionary.
# So, in total 3 dictionaries and 2 lists.
playlists = {"playlist1": playlist,"playlist2": {
"title": "Morning Motivation",
"genre": "Pop",
"songs": ["Rise Up", "Shine Bright", "New Day"],
"duration": 30
}
}

print("\n",playlists)

# gets the first song in the 2nd playlist
print("\nFirst song in second playlist:", playlists["playlist2"]["songs"][0])