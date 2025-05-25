from typing import Dict, List, Optional
from .models import Movie, MovieCollectionIterator

class MovieCollection:
    def __init__(self) -> None:
        self._movies: Dict[str, Movie] = {}
    
    def add_movie(self, movie: Movie) -> None:
        """Добавляет фильм в коллекцию."""
        if movie.title in self._movies:
            raise ValueError(f"Фильм с названием '{movie.title}' уже существует")
        self._movies[movie.title] = movie
    
    def remove_movie(self, title: str) -> None:
        """Удаляет фильм из коллекции."""
        if title not in self._movies:
            raise ValueError(f"Фильм с названием '{title}' не найден")
        del self._movies[title]
    
    def get_movie(self, title: str) -> Optional[Movie]:
        """Возвращает фильм по названию."""
        return self._movies.get(title)
    
    def search_by_title(self, keyword: str) -> List[Movie]:
        """Ищет фильмы по ключевому слову в названии."""
        return [
            movie for title, movie in self._movies.items() 
            if keyword.lower() in title.lower()
        ]
    
    def search_by_year(self, year: int) -> List[Movie]:
        """Ищет фильмы по году выпуска."""
        return [movie for movie in self._movies.values() if movie.year == year]
    
    def search_by_genre(self, genre: str) -> List[Movie]:
        """Ищет фильмы по жанру."""
        return [
            movie for movie in self._movies.values() 
            if genre.lower() in movie.genre.lower()
        ]
    
    def search_by_rating(self, min_rating: float, max_rating: float) -> List[Movie]:
        """Ищет фильмы по рейтингу в диапазоне."""
        return [
            movie for movie in self._movies.values() 
            if min_rating <= movie.rating <= max_rating
        ]
    
    def get_all_movies(self) -> List[Movie]:
        """Возвращает все фильмы в коллекции."""
        return list(self._movies.values())
    
    def __iter__(self) -> MovieCollectionIterator:
        """Возвращает итератор для перебора коллекции."""
        return MovieCollectionIterator(list(self._movies.values()))
    
    def __len__(self) -> int:
        """Возвращает количество фильмов в коллекции."""
        return len(self._movies)
    
    def __contains__(self, title: str) -> bool:
        """Проверяет, есть ли фильм с указанным названием в коллекции."""
        return title in self._movies