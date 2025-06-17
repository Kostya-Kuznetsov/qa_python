import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:
    # для удобства экземпляр класса перед каждым тестом создадим фикстурой в confest.py

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    #1 затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self, collector):



        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2
        assert 'Гордость и предубеждение и зомби' and 'Что делать, если ваш кот хочет вас убить' in collector.get_books_genre()

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    # далее будут мои тесты

    #2 Тест создания книги с невалидным значением по кол-ву символов
    @pytest.mark.parametrize("title", [
        '',  # Пустое название
        'Гордость и предубеждение и зомби живущие на западе'  # Название длиной более 40 символов
    ])

    def test_add_book_invalid_title(self, collector, title):
        start_count = len(collector.get_books_genre())
        collector.add_new_book(title)  # Пытаемся добавить книгу с недопустимым названием
        assert len(collector.get_books_genre()) == start_count  # Количество книг не изменилось

    #3 Тест добавления уже существующей книги
    def test_add_new_book_duplicate(self, collector):
        collector.add_new_book('Хроники Риддика')
        collector.add_new_book('Хроники Риддика')
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize("name, genre", [
        ('Гордость и предубеждение', 'Фантастика'),
        ('1984', 'Фантастика'),
        ('Моби Дик', 'Ужасы')
    ])

    #4 Тест установки жанра для книги
    def test_set_book_genre(self, collector, name, genre):
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    #5 Тест установки жанра для несуществующей книги
    def test_set_book_genre_nonexistent(self, collector):
        collector.set_book_genre('Волшебник изумрудного города', 'Фантастика')
        assert collector.get_book_genre('Волшебник изумрудного города') is None

    #6 Тест получения книг с определённым жанром
    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        collector.add_new_book('Синий трактор')
        collector.set_book_genre('Синий трактор', 'Мультфильмы')

        assert collector.get_books_with_specific_genre('Фантастика') == ['Гарри Поттер']
        assert collector.get_books_with_specific_genre('Ужасы') == ['Сияние']
        assert collector.get_books_with_specific_genre('Мультфильмы') == ['Синий трактор']

    #7 Тест получения жанра книги по её имени
    def test_get_book_genre_by_name(self, collector):
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert collector.get_book_genre('Гарри Поттер') == 'Фантастика'


    #8 Тест получения книг, подходящим детям
    @pytest.mark.parametrize("book_title, genre, expected_in_list", [
        ('Волшебник изумрудного города', 'Фантастика', True),
        ('Загадочное преступление', 'Детективы', False),
        ('Синий трактор', 'Мультфильмы', True),
        ('Мрачные истории', 'Ужасы', False)
    ])
    def test_get_books_for_children(self, collector, book_title, genre, expected_in_list):
        collector.add_new_book(book_title)
        collector.set_book_genre(book_title, genre)
        books_for_children = collector.get_books_for_children()
        assert (book_title in books_for_children) == expected_in_list

    #9 Тест добавления книги в избранное
    def test_add_book_in_favorites(self, collector):

        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        assert 'Гарри Поттер' in collector.get_list_of_favorites_books()

    #10 Тест добавленя несуществующей книги в избранное
    def test_add_book_in_favorites_non_existent_book(self, collector):
        collector.add_book_in_favorites('Несуществующая книга')
        assert len(collector.get_list_of_favorites_books()) == 0

    #11 Тест удаления книги из Избранного
    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Хроники Риддика')
        collector.add_book_in_favorites('Хроники Риддика')
        collector.delete_book_from_favorites('Хроники Риддика')
        assert 'Хроники Риддика' not in collector.get_list_of_favorites_books()

    #12 Тест получения списка Избранных книг

    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book('Хроники Риддика')
        collector.add_book_in_favorites('Хроники Риддика')
        collector.add_new_book('Гарри Поттер')
        collector.add_book_in_favorites('Гарри Поттер')
        collector.add_new_book('Sapiens')
        collector.add_book_in_favorites('Sapiens')
        assert collector.get_list_of_favorites_books() == ['Хроники Риддика', 'Гарри Поттер', 'Sapiens']

    #13 Тест вывода текущего словаря books_genre

    def test_get_books_genre_returns_current_dict(self, collector):
        collector.add_new_book('Хроники Риддика')
        collector.set_book_genre('Хроники Риддика', 'Фантастика')
        collector.add_new_book('Омен')
        collector.set_book_genre('Омен', 'Ужасы')
        assert collector.get_books_genre() == {
            'Хроники Риддика': 'Фантастика',
            'Омен': 'Ужасы'
        }






