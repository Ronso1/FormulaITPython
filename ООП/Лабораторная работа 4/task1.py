class Car:
    """
    Базовый класс "Автомобиль", содержащий общие атрибуты и методы

    """

    def __init__(self, manufacture: str, model: str, year: int, color: str):
        """
        Создание экземпляра класса

        :param manufacture: Название фирмы
        :param model: Название модели
        :param year: Год выпуска
        :param color: Цвет автомобиля
        Пример:
        >>> new_car = Car('Ford', 'Fusion', 2008, 'Красный')
        >>> print(new_car)
        Автомобиль компании Ford, модель Fusion, цвет красный, год выпуска 2008
        """
        self.validate_attributes(manufacture, model, year, color)

        self._manufacture = manufacture
        self._model = model
        self.year = year
        self.color = color

    @property
    def manufacture(self) -> str:
        return self._manufacture

    @property
    def model(self) -> str:
        return self._model

    def validate_attributes(self, manufacture: str, model: str, year: int, color: str) -> None:
        """
        Валидация входных данных

        :param manufacture: Наименование фирмы
        :param model: Наименование модели
        :param year: Год выпуска
        :param color: Цвет автомобиля
        :return:
        """
        if not isinstance(manufacture, str):
            raise TypeError('Название фирмы должно быть строкой.')
        if not isinstance(model, str):
            raise TypeError('Наименование модели должно быть строкой.')
        if not isinstance(year, int):
            raise TypeError('Год выпуска должен быть целым числом.')
        if not isinstance(color, str):
            raise TypeError('Цвет должен быть строкой.')

    def __str__(self) -> str:
        return f'Автомобиль компании {self.manufacture}, модель {self.model}, цвет {self.color.lower()}, год выпуска {self.year}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(manufacture={self._manufacture!r}, model={self._model!r}, color={self.color!r}, year={self.year!r})'

    def is_modern_car(self) -> bool:
        """
        Проверяет, является ли автомобиль современным (год выпуска после 2010)
        Пример:
        >>> new_car = Car('Ford', 'Fusion', 2008, 'Красный')
        >>> new_car.is_modern_car()
        False
        """
        return self.year > 2010


class LightCar(Car):
    """
    Дочерний класс "Легковой автомобиль"
    Расширяет функциональность базового класса "Автомобиль"
    """

    def __init__(self, manufacture: str, model: str, year: int, color: str, horsepower: int):
        """
        Создание экземпляра класса

        :param manufacture: Наименование фирмы
        :param model: Наименование модели
        :param year: Год выпуска
        :param color: Цвет автомобиля
        :param horsepower: Количество лошадиных сил
        Пример:
        >>> light_car = LightCar('Ford', 'Fusion', 2015, 'Синий', 180)
        >>> print(light_car)
        Автомобиль компании Ford, модель Fusion, цвет синий, год выпуска 2015, мощность 180 л.с.
        """
        super().__init__(manufacture, model, year, color)
        self.validate_horsepower(horsepower)
        self._horsepower = horsepower

    @property
    def horsepower(self) -> int:
        return self._horsepower

    def validate_horsepower(self, horsepower: int) -> None:
        """
        Валидация количества лошадиных сил

        :param horsepower: Количество лошадиных сил
        :return:
        """
        if not isinstance(horsepower, int):
            raise TypeError('Количество лошадиных сил должно быть целым числом.')
        if horsepower <= 0:
            raise ValueError('Количество лошадиных сил не может быть меньше или равно 0.')

    def __str__(self) -> str:
        return super().__str__() + f', мощность {self.horsepower} л.с.'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(manufacture={self._manufacture!r}, model={self._model!r}, color={self.color!r}, year={self.year!r}, horsepower={self._horsepower!r})'

    def is_modern_car(self) -> bool:
        """
        Переопределенный метод определения современности автомобиля.
        Учитывает мощность двигателя (современным считается авто после 2010 года и мощностью выше 150 л.с.).
        :return:
        Пример:
        >>> light_car = LightCar('Ford', 'Fusion', 2015, 'Синий', 180)
        >>> light_car.is_modern_car()
        True
        """
        return self.year > 2010 and self.horsepower > 150


class Truck(Car):
    """
    Дочерний класс "Грузовой автомобиль"
    Расширяет функциональность базового класса "Автомобиль"

    """

    def __init__(self, manufacture: str, model: str, year: int, color: str, load_capacity: int):
        """
        Создание экземпляра класса

        :param manufacture: Наименование фирмы
        :param model: Наименование модели
        :param year: Год выпуска
        :param color: Цвет автомобиля
        :param load_capacity:
        Пример:
        >>> truck_car = Truck('Volvo', 'FH16', 2020, 'Белый', 10000)
        >>> print(truck_car)
        Автомобиль компании Volvo, модель FH16, цвет белый, год выпуска 2020, грузоподъемность 10000 кг.
        """
        super().__init__(manufacture, model, year, color)
        self.validate_load_capacity(load_capacity)
        self._load_capacity = load_capacity

    @property
    def load_capacity(self) -> int:
        return self._load_capacity

    def validate_load_capacity(self, load_capacity: int) -> None:
        """
        Валидация грузоподъемности

        :param load_capacity:
        :return:
        """
        if not isinstance(load_capacity, int):
            raise TypeError('Грузоподъемность должна быть целым числом.')
        if load_capacity <= 0:
            raise ValueError('Грузоподъемность не может быть меньше или равна 0.')

    def __str__(self) -> str:
        return super().__str__() + f', грузоподъемность {self.load_capacity} кг.'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}(manufacture={self._manufacture!r}, model={self._model!r}, color={self.color!r}, year={self.year!r}, load_capacity={self._load_capacity!r})'

    def can_carry_load(self, weight: int) -> bool:
        """
        Проверяет, может ли грузовик перевезти заданный вес.

        :param weight: Грузоподъемность грузовика
        Пример:
        >>> truck_car = Truck('Volvo', 'FH16', 2020, 'Белый', 10000)
        >>> truck_car.can_carry_load(5000)
        True
        """
        return weight <= self.load_capacity

    def is_heavy_duty(self) -> bool:
        """
        Проверяет, является ли грузовик тяжелым (грузоподъемность более 5000 кг).

        Пример:
        >>> truck_car = Truck('Volvo', 'FH16', 2020, 'Белый', 10000)
        >>> truck_car.is_heavy_duty()
        True
        """
        return self.load_capacity > 5000


if __name__ == "__main__":
   pass