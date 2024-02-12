class MobileDevice:
    """Класс для представления мобильного устройства."""

    def __init__(self, brand: str, model: str):
        """Инициализирует устройство с основными параметрами."""
        if not isinstance(brand, str) or not isinstance(model, str):
            raise TypeError
        self.brand = brand
        self.model = model

    def __str__(self) -> str:
        """Возвращает строковое представление устройства."""
        return f"{self.brand} {self.model}"

    def __repr__(self) -> str:
        """Возвращает 'официальное' строковое представление объекта."""
        return f"MobileDevice('{self.brand}', '{self.model}')"

    @staticmethod
    def search_internet(request: str) -> str:
        """Поиск в обычном интернет-браузере"""
        if not isinstance(request, str):
            raise TypeError
        return f"Start searching for \"{request}\" in the Internet browser"


class SamsungMobile(MobileDevice):
    def __init__(self, model: str, screen_size: float, camera_resolution: int):
        """Расширяем инициализатор базового класса."""
        if not isinstance(screen_size, float) or not isinstance(camera_resolution, int) or camera_resolution <= 0 or screen_size <= 0:
            raise TypeError
        super().__init__("Samsung", model)
        self.camera_resolution = camera_resolution
        self.os = "Android"
        self.screen_size = screen_size

    def __str__(self) -> str:
        """Перегружаем строковое представление, добавляя информацию."""
        base_str = super().__str__()
        return f"{base_str}, Camera: {self.camera_resolution}MP, Screen Size: {self.screen_size} Inch, Os: {self.os}"

    def __repr__(self) -> str:
        """Перегружаем 'официальное' строковое представление, добавляя информацию."""
        base_repr = super().__repr__()
        return f"SamsungMobile{base_repr[12:-1]}, '{self.screen_size}', '{self.camera_resolution}')"

    @staticmethod
    def screen_edge(mode: bool) -> str:
        """Добавим уникальную для Samsung-телефонов функцию"""
        if not isinstance(mode, bool):
            raise TypeError
        if mode:
            return "Edge screen mode was turned on"
        return "Edge screen mode was turned off"


class AppleMobile(MobileDevice):
    def __init__(self, model: str, screen_size: float, camera_resolution: int):
        """Расширяем инициализатор базового класса."""
        if not isinstance(screen_size, float) or not isinstance(camera_resolution, int) or camera_resolution <= 0 or screen_size <= 0:
            raise TypeError
        super().__init__("Apple", model)
        self.camera_resolution = camera_resolution
        self.os = "IOS"
        self.screen_size = screen_size

    def __str__(self) -> str:
        """Перегружаем строковое представление, добавляя информацию."""
        base_str = super().__str__()
        return f"{base_str}, Camera: {self.camera_resolution}MP, Screen Size: {self.screen_size} Inch, Os: {self.os}"

    def __repr__(self) -> str:
        """Перегружаем 'официальное' строковое представление, добавляя информацию."""
        base_repr = super().__repr__()
        return f"AppleMobile{base_repr[12:-1]}, '{self.screen_size}', '{self.camera_resolution}')"

    @staticmethod
    def search_internet(request: str) -> str:
        """У телефонов компании 'Apple' основной браузер - Safari"""
        if not isinstance(request, str):
            raise TypeError
        return f"Start searching for \"{request}\" in the Safari."


class DigitalPhone(MobileDevice):
    def __init__(self, brand: str, model: str):
        """Инициализирует устройство с основными параметрами."""
        super().__init__(brand, model)

    def __repr__(self) -> str:
        """Перегружаем 'официальное' строковое представление, добавляя информацию."""
        base_repr = super().__repr__()
        return f"DigitalPhone{base_repr[12:]}"

    @staticmethod
    def search_internet(request: str) -> str:
        """Проводные телефоны не могут использовать интернет"""
        return f"Sorry, this phone model can't use the internet."


if __name__ == "__main__":
    samsung = SamsungMobile("Galaxy S23", 7.3, 240)
    iphone = AppleMobile("Iphone 14 Pro", 5.8, 420)
    digital_phone = DigitalPhone("Panasonic", "KX-TS2350RUW")
    print(samsung.search_internet("Python Course"))
    print(samsung.screen_edge(True))
    print(digital_phone.search_internet("HOW TO USE THE INTERNET ON DIGITAL PHONES?"))
    print(iphone.search_internet("I have an iPhone, am I cool now?"))
    print(repr(samsung))
    print(str(samsung))
    print(repr(iphone))
    print(str(iphone))
    print(repr(digital_phone))
    print(str(digital_phone))
    pass
