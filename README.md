## Тест состоит из файлов:
### main.py - класс коллектора
### tests.py - тесты для main.py
### conftest.py - файл с фикстурой def collector, которая создаёт объект класса BooksCollector, чтобы не ### создавать объект на каждом тесте
---
## Описание тестов
### Введение: В примере, который даётся в задании идёт описание класса TestBooksCollector, но в моей реализации от этого класса я отказался, в пользу фикстуры. В всех тестах вместо строки collector == BooksCollector используется фикстура collector


1. **test_add_new_book_add_two_books_books_added** - проверяет метод *def add_new_book* с валидными значениями книг
2. **test_add_new_book_same_book_is_not_added** - проверяет, что книга, которая уже есть в словаре self.books_genre не добавялется повторно
3. **test_add_new_book_negative_input_book_is_not_aded** - проверяет, что нельзя добавить в словарь книги, которые не проходят условаия - использована параметизация
4. **test_set_book_genre_all_genres_setted** - проверяем метод *set_book_genre* с валидным значениями жанров - использована параметизация
5. **test_set_book_genre_negative_input_for_book_name_is_not_setted** - проверяем, что нельзя у становить жанр книгам, которые не были добавлены в self.books_genre
6. **test_set_book_genre_negative_input_for_genre_is_not_setted** - проверяем, что нельзя установить жанр, которого нет в списке self.genre
7. **test_get_books_with_specific_genre_valid_genre_ist_is_emptyd** - проверяем *get_books_with_specific_genre* с валидными значениями
8. **test_get_books_with_specific_genre_negative_genre_are_returned** - проверяем, что если у книги нет жанра, или ей попытались поставить невалидный жанр, то нам вернется пустой список
9. **test_get_books_with_specific_genre_wrong_input_books_list_is_empty** - проверяем, что при попытке установить несуществующей или невалидной книге жанр, нам вернется пустой список
10. **test_get_books_for_children_book_in_list_returned** - проверяем, что *get_books_for_children* возвращает список, если в нём есть подходящие книги
11. **test_get_books_for_children_age_rating_book_is_not_added_to_list** - проверяем, что книги с возрастными ограничениями не добавляются в список
12. **test_get_books_for_children_more_than_one_book_valid_genres_are_added** - проверяем, что при добавлении сразу нескольких книг разных жанров метод вернёт коррректный список
13. **test_add_book_in_favorites_book_is_added** - проверяем, что метод *add_book_in_favorites*, добавляет книгу в список избранного, если книга есть в словаре книг
14. **test_add_book_in_favorites_same_book_is_not_added** - проверяем, что нельзя добавить одну и ту же книгу дважды
15. **test_add_book_in_favorites_invalid_input_book_is_not_added** - проверяем, что невалидные имена не добавляются в список, так как этих имён нет в self.books_genre
16. **test_add_book_in_favorites_more_than_one_book_is_added** - проверяем добавление сразу нескольких книг в избранное
17. **test_delete_book_from_favorites_book_is_deleted** - проверяем, что метод *delete_book_from_favorites* удаляе книгу из избранного
18. **test_delete_book_from_favorites_book_not_in_favorites_None** - проверяем, что нельзя удалить книгу из избранного которой нет в избранном
19. **test_get_book_genre_valid_genre_book_is_returned** - проверяем, что метдод *get_book_genre* возвращает жанр по имени книги
20. **test_get_book_genre_wrong_genre_empty_genre_returned** - проверяем, что если у книги нет жанра или ей был задан невалидный жанр, то метож вернёт пустую строку

## В итоге реализованы тесты по покрытия всего функционала, по pytest --cov покрытие составляет 100%, по --cov-branch не покрыто строки 28, 27, но пока не совсем разобрался как мне их покрыть