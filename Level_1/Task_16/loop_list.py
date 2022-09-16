# List of my top picks of the best movies ever
list_of_movies = ["Sharknado", "Sharknado 2: The Second One", "Sharknado: Feeding Frenzy","Sharknado 3: Oh Hell No!","Sharknado: The 4th Awakens"]

# Looping over list using enumerate
for index_movie, movie in enumerate(list_of_movies):
    # Plus one added to get the number instead of index position.
    print(f"Movie {index_movie + 1}: {movie}")
