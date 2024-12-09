import random
import doctest

class Book:
    def __init__(self, author: str, title: str, paper_counts: int):
        """
        Создание и инициализация объекта "Книга"

        :param author: ФИО автора книги
        :param title: Название книги
        :param paper_counts: Количество страниц
        Пример:
        >>> new_book = Book('Иван Сергеевич Тургенев', 'Муму', 224)
        """
        self.validate_information(author, title, paper_counts)

        self.author = author
        self.title = title
        self.paper_counts = paper_counts

    def validate_information(self, author, title, paper_counts) -> None:
        if not isinstance(author, str):
            raise TypeError('ФИО автора указывается через string')

        if not isinstance(title, str):
            raise TypeError('Название книги должно быть указано через string')

        if not isinstance(paper_counts, int):
            raise TypeError('Количество страниц книги должно быть указано через int')
        if int(paper_counts) < 0:
            raise ValueError('Количество страниц в книги не может быть меньше 0')

    def is_empty_book(self) -> bool:
        """
        Функция, которая проверяет, имеет ли книга хотя бы одну страницу.

        :return: Является ли данная книга пустой.

        Пример:
        >>> new_book = Book('Иван', 'Невышедшая книга', 0)
        >>> new_book.is_empty_book()
        True
        """
        if self.paper_counts == 0:
            return True
        else:
            return False

    def is_large_book(self) -> bool:
        """
        Функция, которая проверяет, является ли книга большой по количеству страниц.

        :return: Является ли данная книга большой.

        Пример:
        >>> new_book = Book('Иван', 'Невышедшая книга', 55)
        >>> new_book.is_large_book()
        True
        """
        if self.paper_counts > 50:
            return True
        else:
            return False

    def is_unknown_author(self) -> bool:
        """
        Функция, которая проверяет наличие автора.

        :return: Написана ли книга неизвестным автором.

        Пример:
        >>> new_book = Book('', 'Книга без названия', 150)
        >>> new_book.is_unknown_author()
        True
        """

        if self.author == '':
            return True
        else:
            return False


class IDCard:
    def __init__(self, id_card: int, cardholder_name: str, role: str):
        """
        Создание и инициализация объекта "ID карта"

        :param id_card: Номер карты
        :param cardholder_name: ФИО владельца карты
        :param role: Должность

        Пример:
        >>> new_id_card = IDCard(123, 'Ben', 'Рабочий')
        """
        self.validate_dates(id_card, cardholder_name, role)

        self.id_card = id_card
        self.cardholder_name = cardholder_name
        self.role = role

    def validate_dates(self, id_card, cardholder_name, role) -> None:
        if not isinstance(id_card, int):
            raise TypeError("ID карты должно быть задано через int")
        if id_card < 0:
            raise ValueError("ID карты не может быть отрицательным числом")

        if not isinstance(cardholder_name, str):
            raise TypeError("Имя владельца карты задается через string")

        if not isinstance(role, str):
            raise TypeError("Должность владельца карты задается через string")

    def is_worker(self) -> bool:
        """
        Функция, которая проверяет, является ли владелец карты сотрудником

        :return: Является ли владелец карты сотрудником

        Пример:
        >>> new_id_card = IDCard(123, "Ben", "Рабочий")
        >>> new_id_card.is_worker()
        True
        """
        if self.role == "Рабочий":
            return True
        else:
            return False

    def is_admin(self) -> bool:
        """
        Функция, которая проверяет, является ли владелец карты администратором

        :return: Является ли владелец карты администратором

        Пример:
        >>> new_id_card = IDCard(123, "Ben", "Рабочий")
        >>> new_id_card.is_admin()
        False
        """
        if self.id_card == 0:
            return True
        else:
            return False

    def generate_new_id_number(self) -> None:
        """
        Функция, которая генерирует новый номер карты

        :return: Ничего не возвращает, просто изменяет значение атрибута id_card

        Пример:
        >>> new_id_card = IDCard(123, "Ben", "Рабочий")
        >>> new_id_card.generate_new_id_number()
        """
        self.id_card = random.randint(1, 999)


class Monitor:
    def __init__(self, resolution_width: int, resolution_height: int, update_rate: int, matrix_type: str):
        """
        Создание и инициализация объекта "Монитор"

        :param resolution_width: Ширина разрешения экрана
        :param resolution_height: Высота разрешения экрана
        :param update_rate: Частота обновления экрана
        :param matrix_type: Тип матрицы

        Пример:
        >>> new_monitor = Monitor(1920, 1080, 75, 'TN')
        """
        self.validate_dates(resolution_width, resolution_height, update_rate, matrix_type)

        self.resolution_width = resolution_width
        self.resolution_height = resolution_height
        self.update_rate = update_rate
        self.matrix_type = matrix_type

    def validate_dates(self, resolution_width, resolution_height, update_rate, matrix_type):
        if not isinstance(resolution_width, int) or not isinstance(resolution_height, int):
            TypeError("Разрешение экрана задается строго через int")
        if resolution_height <= 0 or resolution_width <= 0:
            ValueError("Разрешение экрана не может быть меньше или равно 0")

        if not isinstance(update_rate, int):
            TypeError("Частота обновления дисплея задается строго через int")
        if update_rate < 30:
            ValueError("Такой частоты обновления монитора не существует в природе")

        if not isinstance(matrix_type, str):
            TypeError("Тип матрицы указывается строго через str")

    def is_old_monitor(self) -> bool:
        """
        Функция, которая проверяет, является ли монитор старым или нет

        :return: Является ли монитор старым или нет

        Пример:
        >>> new_monitor = Monitor(1920, 1080, 75, 'TN')
        >>> new_monitor.is_old_monitor()
        False
        """
        if self.resolution_width <= 800 or self.resolution_height <= 600:
            return True
        else:
            return False

    def is_modern_monitor(self) -> bool:
        """
        Функция, которая проверяет, является ли монитор современным или нет

        :return: Является ли монитор современным или нет

        Пример:
        >>> new_monitor = Monitor(1920, 1080, 75, 'TN')
        >>> new_monitor.is_modern_monitor()
        True
        """
        if self.resolution_width >= 1920 or self.resolution_height >= 1080:
            return True
        else:
            return False

    def is_TN_matrix(self) -> bool:
        """
        Функция, которая проверяет конкретный тип матрицы монитора (TN)

        :return: Матрица монитора - TN

        Пример:
        >>> new_monitor = Monitor(1920, 1080, 75, 'TN')
        >>> new_monitor.is_TN_matrix()
        True
        """
        if self.matrix_type.upper() == 'TN':
            return True
        else:
            return False


if __name__ == "__main__":
    doctest.testmod()