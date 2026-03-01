movie_genres = ("Action", "Comedy", "Drama", "Horror", "Sci-Fi")

# Write your code here
temp_list = list(movie_genres)

temp_list[2] = "Thriller"  
temp_list[-2] = "Adventure"  

movie_genres = tuple(temp_list)

del temp_list

# Testing
print("Updated genres:", movie_genres)

# current_movies = ("Inception", "Interstellar", "Tenet", "Dunkirk")

# Step 1: Convert the tuple to a list
# movies_list = list(current_movies)

# Step 2: Update the second and third movie titles
#movies_list[1] = "Memento"
#movies_list[2] = "The Prestige"

# Step 3: Convert the list back to a tuple
#current_movies = tuple(movies_list)

#print(current_movies)