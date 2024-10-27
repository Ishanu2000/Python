#Represent a movie with a title, genre, and rating
class Movie:
    def __init__(self, title, genre, rating):
        self.title = title
        self.genre = genre
        self.rating = rating

#Manage a movie database
class MovieDatabase:
    def __init__(self):
        self.movies = []  #List to store all movie objects
        self.genres = set()  #Set to store unique genres

    #Add a movie to the database
    def add_movie(self, movie):
        self.movies.append(movie)
        self.genres.add(movie.genre)  #Add genre to the set of unique genres
        print(f"Movie '{movie.title}' added to the database.")

    #Search for movies by genre
    def search_by_genre(self, genre):
        print(f"\n----- Movies in the genre '{genre}' -----")
        found = False
        for movie in self.movies:
            if movie.genre.lower() == genre.lower():
                print(f"- {movie.title} (Rating: {movie.rating})")
                found = True
        if not found:
            print("No movies found in this genre.")

    #Display all movies sorted by rating (highest to lowest)
    def display_movies_by_rating(self):
        print("\n----- Movies sorted by rating -----")
        #Sorting movies by rating in descending order
        sorted_movies = sorted(self.movies, key=lambda x: x.rating, reverse=True)
        for movie in sorted_movies:
            print(f"{movie.title} - Genre: {movie.genre}, Rating: {movie.rating}")

    #Display all unique genres in the database
    def display_genres(self):
        print("\n----- Unique Genres in Database -----")
        for genre in sorted(self.genres):  #Sorting genres alphabetically
            print(f"- {genre}")

#Example
#Create a MovieDatabase instance
movie_db = MovieDatabase()

#Add movies to the database
movie_db.add_movie(Movie("Inception", "Sci-Fi", 8.8))
movie_db.add_movie(Movie("The Dark Knight", "Action", 9.0))
movie_db.add_movie(Movie("Interstellar", "Sci-Fi", 8.6))
movie_db.add_movie(Movie("The Godfather", "Crime", 9.2))
movie_db.add_movie(Movie("Pulp Fiction", "Crime", 8.9))

#Search for movies by genre
movie_db.search_by_genre("Sci-Fi")

#Display all movies sorted by rating
movie_db.display_movies_by_rating()

#Display all unique genres
movie_db.display_genres()
