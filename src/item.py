from csv import DictReader
from pathlib import Path


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}(\'{self.__name}\', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        raise Exception(ValueError, "Складывать можно только объекты Item и дочерние от них")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return round(self.price * self.quantity, 2)

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = round(self.price * Item.pay_rate, 2)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) > 10:
            self.__name = value[:10]
        else:
            self.__name = value

    @classmethod
    def instantiate_from_csv(cls, file_path: str) -> None:
        """Инициализирует экземпляры класса Item по данным из CSV-файла."""
        Item.all = []
        file_path = Path(__file__).parent.parent / file_path
        with open(file_path) as file:
            data = DictReader(file)
            for row in data:
                name = row['name']
                price = float(row['price'])
                quantity = Item.string_to_number(row['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(value: str) -> int:
        """
        Преобразует строку в число округляя до целой части.
        """
        return int(float(value) // 1)
