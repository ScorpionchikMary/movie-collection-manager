from typing import Iterator

class Movie:
    def __init__(self, title: str, year: int, director: str, genre: str, rating: float):
        self.title = title
        self.year = year
        self.director = director
        self.genre = genre
        self.rating = rating

class MovieCollectionIterator(Iterator[Movie]):
    def __init__(self, movies: list[Movie]):
        self._movies = movies
        self._index = 0
    
    def __next__(self) -> Movie:
        if self._index < len(self._movies):
            movie = self._movies[self._index]
            self._index += 1
            return movie
        raise StopIteration