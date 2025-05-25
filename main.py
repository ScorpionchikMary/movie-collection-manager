from models import Movie
from collection import MovieCollection

if __name__ == "__main__":
    # Создаем коллекцию
    collection = MovieCollection()
    
    # Добавляем фильмы
    collection.add_movie(Movie("The Shawshank Redemption", 1994, "Frank Darabont", "Drama", 9.3))
    collection.add_movie(Movie("The Godfather", 1972, "Francis Ford Coppola", "Crime", 9.2))
    collection.add_movie(Movie("The Dark Knight", 2008, "Christopher Nolan", "Action", 9.0))
    
    # Выводим все фильмы
    print("Все фильмы в коллекции:")
    for movie in collection:
        print(movie)
    
    # Поиск по жанру
    print("\nФильмы в жанре 'Drama':")
    for movie in collection.search_by_genre("Drama"):
        print(movie)
    
    # Поиск по году
    print("\nФильмы 2008 года:")
    for movie in collection.search_by_year(2008):
        print(movie)
    
    # Удаление фильма
    collection.remove_movie("The Godfather")
    print(f"\nПосле удаления, количество фильмов: {len(collection)}")
    
    # Проверка наличия фильма
    print("\nЕсть ли 'The Dark Knight' в коллекции?", "The Dark Knight" in collection)