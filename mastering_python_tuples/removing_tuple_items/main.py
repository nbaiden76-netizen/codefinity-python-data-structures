movie_poster = ('The Lion King', 'Jurassic Park', 'Finding Nemo', '2001: A Space Odyssey', 'Interstellar', 'Gravity', 'The Martian')

# Write your code here
temp_list = list(movie_poster)
temp_list.remove('The Lion King')
temp_list.remove('Jurassic Park')

movie_poster = tuple(temp_list)
del temp_list

# Testing 
print("Updated movie poster:", movie_poster)

#movies = ("Inception", "Interstellar", "Tenet", "Dunkirk", "Memento")

# Deleting the tuple
#del movies

# Attempting to print the deleted tuple will raise an error
#print(movies)

#movies = ("Inception", "Interstellar", "Tenet", "Dunkirk", "Memento")

# Convert the tuple to a list
#movies_list = list(movies)

# Remove specific items
#movies_list.remove("Tenet")
#movies_list.remove("Dunkirk")

# Convert the list back to a tuple
#movies = tuple(movies_list)

#print(movies)