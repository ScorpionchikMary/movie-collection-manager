import unittest
from models import Movie
from collection import MovieCollection

class TestMovie(unittest.TestCase):
    """Тесты для класса Movie"""
    
    def test_positive_movie_creation(self):
        """Позитивный тест: создание объекта Movie с корректными данными"""
        movie = Movie("Inception", 2010, "Christopher Nolan", "Sci-Fi", 8.8)
        self.assertEqual(movie.title, "Inception")
        self.assertEqual(movie.year, 2010)
        self.assertEqual(movie.director, "Christopher Nolan")
        self.assertEqual(movie.genre, "Sci-Fi")
        self.assertEqual(movie.rating, 8.8)
    
    def test_negative_movie_creation(self):
        """Негативный тест: попытка создания с некорректными типами данных"""
        with self.assertRaises(TypeError):
            Movie(123, "2010", 123, True, "8.8")  # Все параметры неверного типа

class TestMovieCollectionPositive(unittest.TestCase):
    """Позитивные тесты для MovieCollection"""
    
    def setUp(self):
        self.collection = MovieCollection()
        self.movies = [
            Movie("Inception", 2010, "Christopher Nolan", "Sci-Fi", 8.8),
            Movie("The Shawshank Redemption", 1994, "Frank Darabont", "Drama", 9.3),
            Movie("The Godfather", 1972, "Francis Ford Coppola", "Crime", 9.2)
        ]
        for movie in self.movies:
            self.collection.add_movie(movie)
    
    def test_add_movie_success(self):
        """Позитивный тест: успешное добавление фильма"""
        new_movie = Movie("Pulp Fiction", 1994, "Quentin Tarantino", "Crime", 8.9)
        initial_count = len(self.collection)
        self.collection.add_movie(new_movie)
        self.assertEqual(len(self.collection), initial_count + 1)
    
    def test_remove_movie_success(self):
        """Позитивный тест: успешное удаление фильма"""
        initial_count = len(self.collection)
        self.collection.remove_movie("Inception")
        self.assertEqual(len(self.collection), initial_count - 1)
    
    def test_search_existing_movie(self):
        """Позитивный тест: поиск существующего фильма"""
        results = self.collection.search_by_title("Inception")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].director, "Christopher Nolan")
    
    def test_iterator_implementation(self):
        """Позитивный тест: проверка работы итератора"""
        movies = list(self.collection)
        self.assertEqual(len(movies), 3)
    
    def test_len_implementation(self):
        """Позитивный тест: проверка длины коллекции"""
        self.assertEqual(len(self.collection), 3)

class TestMovieCollectionNegative(unittest.TestCase):
    """Негативные тесты для MovieCollection"""
    
    def setUp(self):
        self.empty_collection = MovieCollection()
        self.collection = MovieCollection()
        self.movie = Movie("Inception", 2010, "Christopher Nolan", "Sci-Fi", 8.8)
        self.collection.add_movie(self.movie)
    
    def test_add_duplicate_movie(self):
        """Негативный тест: добавление дубликата фильма"""
        with self.assertRaises(ValueError):
            self.collection.add_movie(self.movie)
    
    def test_remove_nonexistent_movie(self):
        """Негативный тест: удаление несуществующего фильма"""
        with self.assertRaises(ValueError):
            self.collection.remove_movie("Nonexistent Movie")
    
    def test_search_empty_collection(self):
        """Негативный тест: поиск в пустой коллекции"""
        results = self.empty_collection.search_by_title("Anything")
        self.assertEqual(len(results), 0)
    
    def test_get_nonexistent_movie(self):
        """Негативный тест: получение несуществующего фильма"""
        self.assertIsNone(self.collection.get_movie("Nonexistent Movie"))
    
    def test_add_invalid_movie_type(self):
        """Негативный тест: добавление не-Movie объекта"""
        with self.assertRaises(TypeError):
            self.collection.add_movie("Not a movie object")
    
    def test_search_invalid_year(self):
        """Негативный тест: поиск по некорректному году"""
        with self.assertRaises(TypeError):
            self.collection.search_by_year("not a number")  # type: ignore
    
    def test_edge_case_empty_string_search(self):
        """Граничный случай: поиск по пустой строке"""
        results = self.collection.search_by_title("")
        self.assertEqual(len(results), 1)  # Должен найти все фильмы
    
    def test_edge_case_high_rating(self):
        """Граничный случай: поиск по очень высокому рейтингу"""
        results = self.collection.search_by_rating(10.0, 10.0)
        self.assertEqual(len(results), 0)

class TestMovieCollectionEdgeCases(unittest.TestCase):
    """Тесты для граничных случаев"""
    
    def setUp(self):
        self.collection = MovieCollection()
        # Фильм с минимально возможными значениями
        self.collection.add_movie(Movie("A", 1900, "A", "A", 0.1))
        # Фильм с максимально возможными значениями
        self.collection.add_movie(Movie("Z"*100, 2100, "Z"*50, "Z"*20, 10.0))
    
    def test_min_values(self):
        """Граничный случай: фильм с минимальными значениями атрибутов"""
        movie = self.collection.get_movie("A")
        self.assertEqual(movie.year, 1900)
        self.assertEqual(movie.rating, 0.1)
    
    def test_max_values(self):
        """Граничный случай: фильм с максимальными значениями атрибутов"""
        movie = self.collection.get_movie("Z"*100)
        self.assertEqual(movie.year, 2100)
        self.assertEqual(movie.rating, 10.0)

if __name__ == "__main__":
    unittest.main(verbosity=2)