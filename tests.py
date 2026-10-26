import pytest

from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_add_two_books_books_added(self, collector):

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_same_book_is_not_added(self, collector):

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('id_input', ['', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'])
    def test_add_new_book_negative_input_book_is_not_aded(self, collector, id_input):
            
        collector.add_new_book(id_input)
        assert len(collector.get_books_genre()) == 0

    @pytest.mark.parametrize('all_genres', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_all_genres_setted(self, collector, all_genres):
        book_name = 'Новая книга'
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, all_genres)
        books_in_genre = collector.get_books_with_specific_genre(all_genres)
        assert book_name in books_in_genre

    @pytest.mark.parametrize('id_input', ['', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'])
    def test_set_book_genre_negative_input_for_book_name_is_not_setted(self, collector, id_input):

        collector.add_new_book(id_input)
        collector.set_book_genre(id_input, 'Фантастика')
        assert collector.get_book_genre(id_input) == None

    @pytest.mark.parametrize('id_input', ['', 'Романтик'])
    def test_set_book_genre_negative_input_for_genre_is_not_setted(self, collector, id_input):
            
        collector.add_new_book('50 оттенков серого')
        collector.set_book_genre('50 оттенков серого', id_input)
        assert collector.get_book_genre('50 оттенков серого') == ''

    def test_get_books_with_specific_genre_valid_genre_returned(self, collector):
            
        collector.add_new_book('Шрэк')
        collector.set_book_genre('Шрэк', 'Мультфильмы')
        movie = ['Шрэк']
        assert movie == collector.get_books_with_specific_genre('Мультфильмы')

    @pytest.mark.parametrize('id_input', ['', 'Нежанр'])
    def test_get_books_with_specific_genre_negative_genre_list_is_empty(self, collector, id_input):

        collector.add_new_book('Самая лучшая книга')
        collector.set_book_genre('Самая лучшая книга', id_input)
        assert collector.get_books_with_specific_genre(id_input) == []

    @pytest.mark.parametrize('id_input', ['', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'])
    def test_get_books_with_specific_genre_wrong_input_books_list_is_empty(self, collector, id_input):

        collector.add_new_book(id_input)
        collector.set_book_genre(id_input, 'Комедия')
        assert collector.get_books_with_specific_genre('Комедия') == []

    def test_get_books_for_children_book_in_list_returned(self, collector):

        collector.add_new_book('Самая лучшая книга')
        collector.set_book_genre('Самая лучшая книга', 'Мультфильмы')
        book = ['Самая лучшая книга']
        assert book == collector.get_books_for_children()

    @pytest.mark.parametrize('not_kids_genres', ['Ужасы', 'Детектив'])
    def test_get_books_for_children_age_rating_book_is_not_added_to_list(self, collector, not_kids_genres):
            
        collector.add_new_book('Самая лучшая книга')
        collector.set_book_genre('Самая лучшая книга', not_kids_genres)
        assert len(collector.get_books_for_children()) == 0

    def test_get_books_for_children_more_than_one_book_valid_genres_are_added(self, collector):
                    
        collector.add_new_book('Самая лучшая книга')
        collector.set_book_genre('Самая лучшая книга', 'Ужасы')
        collector.add_new_book('Шрэк')
        collector.set_book_genre('Шрэк', 'Мультфильмы')
        collector.add_new_book('Тупой и еще тупее')
        collector.set_book_genre('Тупой и еще тупее', 'Комедии')
        collector.add_new_book('Шэрлок Холмс')
        collector.set_book_genre('Шэрлок Холмс', 'Детектив')
        collector.add_new_book('Я робот')
        collector.set_book_genre('Я робот', 'Фантастика')
        book = ['Шрэк', 'Тупой и еще тупее', 'Я робот']
        assert collector.get_books_for_children() == book

    def test_add_book_in_favorites_book_is_added(self, collector):

        collector.add_new_book('Моя любимая книга')
        loved_books = ['Моя любимая книга']
        collector.add_book_in_favorites('Моя любимая книга')
        assert loved_books == collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_same_book_is_not_added(self, collector):

        collector.add_new_book('Моя любимая книга')
        loved_books = ['Моя любимая книга']
        collector.add_book_in_favorites('Моя любимая книга')
        collector.add_book_in_favorites('Моя любимая книга')
        assert loved_books == collector.get_list_of_favorites_books()

    @pytest.mark.parametrize('id_input', ['', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',])
    def test_add_book_in_favorites_invalid_input_book_is_not_added(self, collector, id_input):

        collector.add_new_book(id_input)
        collector.add_book_in_favorites(id_input)
        collector.add_book_in_favorites('Книги нет в словаре')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_add_book_in_favorites_more_than_one_book_is_added(self, collector):

        collector.add_new_book('Моя любимая книга')
        collector.add_new_book('Моя любимая книга 2')
        collector.add_book_in_favorites('Моя любимая книга')
        collector.add_book_in_favorites('Моя любимая книга 2')
        loved_books = ['Моя любимая книга', 'Моя любимая книга 2']
        assert loved_books == collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_book_is_deleted(self, collector):

        collector.add_new_book('Не моя любимая книга')
        collector.add_book_in_favorites('Не моя любимая книга')
        collector.add_new_book('Моя любимая книга')
        collector.add_book_in_favorites('Моя любимая книга')
        collector.delete_book_from_favorites('Не моя любимая книга')
        deleted_book = 'Не моя любимая книга'
        assert deleted_book not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_book_not_in_favorites_None(self, collector):

        collector.add_new_book('Не моя любимая книга')
        collector.add_new_book('Моя любимая книга')
        collector.add_book_in_favorites('Моя любимая книга')
        assert collector.delete_book_from_favorites('Не моя любимая книга') == None

    def test_get_book_genre_valid_genre_book_is_returned(self, collector):
            
        collector.add_new_book('Книжная книга')
        collector.set_book_genre('Книжная книга', 'Фантастика')
        assert collector.get_book_genre('Книжная книга') == 'Фантастика'

    def test_get_book_genre_wrong_genre_empty_genre_returned(self, collector):

        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Романтики')
        assert collector.get_book_genre('Книга') == ''

    def test_get_books_genre_valid_book_returned(self, collector):
        collector.add_new_book('Книга')
        books = {'Книга': ''}
        assert collector.get_books_genre() == books

    @pytest.mark.parametrize('id_input', ['', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',])
    def test_get_books_genre_invalid_input_empty_dict_returned(self, collector, id_input):
        collector.add_new_book(id_input)
        books = {}
        assert collector.get_books_genre() == books
    
    def test_get_list_of_favorites_books_valid_books_returned(self, collector):
        collector.add_new_book('Моя любимая книга')
        collector.add_new_book('Моя любимая книга 2')
        collector.add_book_in_favorites('Моя любимая книга')
        collector.add_book_in_favorites('Моя любимая книга 2')
        favorite_books = ['Моя любимая книга','Моя любимая книга 2']
        assert collector.get_list_of_favorites_books() == favorite_books

    @pytest.mark.parametrize('id_input', ['', 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa',])
    def test_get_list_of_favorites_books_invalid_books_empty_list_returned(self, collector, id_input):
        collector.add_new_book(id_input)
        collector.add_book_in_favorites(id_input)
        favorite_books = []
        assert collector.get_list_of_favorites_books() == favorite_books