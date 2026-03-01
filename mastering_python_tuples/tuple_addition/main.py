animal_movies = ('The Lion King', 'Jurassic Park', 'Finding Nemo')

# Write your code here
# adding tuples together 
#new_movies = ('Dumbo', 'Zootopia')

#animal_movies += new_movies

# Converting to lists then using append to create a tuple 

new_movies = list(animal_movies)
new_movies.append('Dumbo')
new_movies.append('Zootopia')
animal_movies = tuple(new_movies)

print("Updated animal movies:", animal_movies)

# Original tuple of movies
#movies = ("Inception", "Interstellar", "Tenet")

# Convert the tuple to a list
#movies_list = list(movies)

# Add a new movie to the list
#movies_list.append("Dunkirk")

# Convert the list back to a tuple
#movies = tuple(movies_list)

#print("After:", movies)

# Original tuple of movies
#movies = ("Inception", "Interstellar", "Tenet")

# Create a new tuple with the movie to add
#new_movies = ("Dunkirk",)

# Concatenate the tuples
#movies += new_movies

#print(movies)