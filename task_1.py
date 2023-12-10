import doctest


class SmartPhone:
    def __init__(self, os: str, version: (int, float), cameras: int):
        """
        Создание и подготовка к работе объекта "Смартфон"

        :param os: Какую операционную систему использует телефон
        :param version: Какая версия операционной системы на телефоне
        :param cameras: Сколько камер у телефона

        Примеры:
        >>> smartphone = SmartPhone("Android", 18.1, 4)  # инициализация экземпляра класса
        """
        if not isinstance(os, str) or not isinstance(version, (int, float)) or not isinstance(cameras, int):
            raise TypeError
        self.os = os
        self.version = version
        self.cameras = cameras

    def choose_version(self, version: (int, float)):
        """
        Функция которая меняет версию операционной системы телефона

        :param version: Какую версию ос будет использовать телефон
        :raise TypeError: Если новая версия не int или float, то вызываем ошибку

        Примеры:
        >>> smartphone = SmartPhone("Android", 18.1, 4)
        >>> smartphone.choose_version(20.2)
        """
        # Выбираем версию операционной системы, которую хотим использовать
        if not isinstance(version, (int, float)):
            raise TypeError
        if not 8.1 <= version <= 20.4:
            raise ValueError
        self.version = version

    def quantity_of_cameras(self) -> int:
        """
        Функция которая возвращает количество камер у телефона

        :return: количество камер

        Примеры:
        >>> smartphone = SmartPhone("Android", 18.1, 4)
        >>> smartphone.quantity_of_cameras()
        """
        ...
        # return self.cameras


class Restaurant:
    def __init__(self, rank: int, county_of_kitchen: str, available_now: bool):
        """
        Создание и подготовка к работе объекта "Ресторан"

        :param rank: Количество звезд у ресторана
        :param county_of_kitchen: Какой народной культуре принадлежит ресторан
        :param available_now: Открыт (доступен) ли сейчас ресторан

        Примеры:
        >>> restaurant = Restaurant(4, "France", True)  # инициализация экземпляра класса
        """
        if not isinstance(rank, int):
            raise TypeError
        if not isinstance(county_of_kitchen, str):
            raise TypeError
        if not 1 <= rank <= 5:
            raise ValueError
        if not isinstance(available_now, bool):
            raise TypeError

        self.rank = rank
        self.country_of_kitchen = county_of_kitchen
        self.average_bill = rank * 500
        self.available_now = available_now

    def get_average_bill(self) -> (int, float):
        """
        Функция которая считает и возвращает средний чек ресторана

        :return: Средний чек ресторана

        Примеры:
        >>> restaurant = Restaurant(4, "France", True)
        >>> restaurant.get_average_bill()
        """
        if self.country_of_kitchen == "France":
            ...
            # return self.average_bill + 200 if self.rank <= 3 else self.average_bill + 500
        else:
            ...
            # return self.average_bill

    def change_average_bill(self, new_average: (int, float)):
        """
        Функция которая меняет средний чек ресторана

        :param new_average: Новый средний чек

        Примеры:
        >>> restaurant = Restaurant(4, "France", True)
        >>> restaurant.change_average_bill(1500)
        """
        if not isinstance(new_average, (int, float)):
            raise TypeError
        self.average_bill = new_average

    def open_restaurant(self):
        """
        Функция которая открывает ресторан (становится доступным)

        :raise ValueError: Если ресторан уже открыт, то вызываем ошибку

        Примеры:
        >>> restaurant = Restaurant(4, "France", False)
        >>> restaurant.open_restaurant()
        """
        if self.available_now:
            raise ValueError("Restaurant already opened!")
        self.available_now = True

    def close_restaurant(self):
        """
        Функция которая закрывает ресторан (становится недоступным)

        :raise ValueError: Если ресторан уже закрыт, то вызываем ошибку

        Примеры:
        >>> restaurant = Restaurant(4, "France", True)
        >>> restaurant.change_average_bill(1500)
        """
        if not self.available_now:
            raise ValueError("Restaurant already closed!")
        self.available_now = False


class Student:
    def __init__(self, first_name: str, last_name: str, age: int, course: int, profession: (str, type(None)) = None):
        """
        Создание и подготовка к работе объекта "Студент"

        :param first_name: Имя студента
        :param last_name: Фамилия студента
        :param age: Возраст студента в годах
        :param course: Курс студента
        :param profession: Профессия (работа) студента

        Примеры:
        >>> student = Student("Mikhail", "Buzmakov", 20, 3)  # инициализация экземпляра класса
        """
        if not isinstance(first_name, str):
            raise TypeError
        if not isinstance(last_name, str):
            raise TypeError
        if not isinstance(age, int):
            raise TypeError
        if not isinstance(course, int):
            raise TypeError
        if not isinstance(profession, (str, type(None))):
            raise TypeError
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.course = course
        self.profession = profession

    def give_profession(self, profession: str):
        """
        Функция которая дает студенту работу

        :param profession: (Новая) Профессия студента

        Примеры:
        >>> student = Student("Mikhail", "Buzmakov", 20, 3)
        >>> student.give_profession("Programmer")
        """
        if not isinstance(profession, str):
            raise TypeError
        self.profession = profession

    def get_age(self):
        """
        Функция которая возвращает возраст студента в годах

        :return: Возраст студента в годах

        Примеры:
        >>> student = Student("Mikhail", "Buzmakov", 20, 3, "Janitor")
        >>> student.get_age()
        """
        # return self.age
        ...

    def happy_birthday(self):
        """
        Функция которая отмечает день рождение (увеличивает возраст на 1)!

        Примеры:
        >>> student = Student("Mikhail", "Buzmakov", 20, 3, "Plant Worker")
        >>> student.happy_birthday()
        """
        self.age += 1

    def successful_two_session(self):
        """
        Функция которая успешно заканчивает курс (увеличивает курс на 1)

        Примеры:
        >>> student = Student("Mikhail", "Buzmakov", 20, 3)
        >>> student.successful_two_session()
        """
        self.course += 1

    def new_last_name(self, last_name: str):
        """
        Функция которая меняет фамилию

        Примеры:
        >>> student = Student("Mikhail", "Buzmakov", 20, 3)
        >>> student.new_last_name("Vokamzub")
        """
        if not isinstance(last_name, str):
            raise TypeError
        self.last_name = last_name


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
