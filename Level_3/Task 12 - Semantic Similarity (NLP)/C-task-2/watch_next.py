import spacy
nlp = spacy.load('en_core_web_md')

watched_movie = """Planet Hulk :
Will he save their world or destroy it? When the Hulk becomes too dangerous for the
Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet 
here the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where
he is sold into slavery and trained as a gladiator."""

# returns a list of tuples with the movie name and description
def movies():
    with open("movies.txt", "r") as f:
        movies = [tuple(movie.split(":")) for movie in f.readlines()]
    return movies

# Returns the single movie recommended
def movie_to_recommend(movie, movies):
    model_movie = nlp(movie)
    scores = []
    movie_names = []
    for movie_rec in movies:
            similarity = nlp(movie_rec[1]).similarity(model_movie)
            scores.append(similarity)
            movie_names.append(movie_rec[0])
    # Putting movies into a dictionary then sorting them into ascending
    # order and returning the key of the last dictionary entry
    return sorted(
        {movie_names[i]:scores[i] for i in range(len(movie_names))}.items(), 
        key=lambda x:x[1])[-1][0]

# Main function
def main():
    print("We recommend that you watch this movie!")
    print(movie_to_recommend(movie=watched_movie, movies=movies()))

# Run this script
if __name__ == "__main__":
    main()


    
