from models import Movie
from collection import MovieCollection

def main():
    collection = MovieCollection()
    collection.add_movie(Movie("Inception", 2010, "Christopher Nolan", "Sci-Fi", 8.8))
    # Добавьте другие примеры

if __name__ == "__main__":
    main()