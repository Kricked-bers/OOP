from abc import ABC


class Category:
    # Атрибуты класса
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        # Атрибуты экземпляра
        self.name = name
        self.description = description
        self.__products = products

    def add_product(self, new_product):
        # Функция добавления продукта
        if issubclass(new_product.__class__, Product):
            return self.__products.append(new_product)
        else:
            raise TypeError

    def __str__(self):
        return (
            f"{self.name}, количество продуктов: "
            f"{sum([i.quantity for i in self.__products])} шт."
        )

    @property
    def products(self):
        return self.__products

    def middle_price(self):
        try:
            ave_prices = sum([i.price for i in self.__products]) / len(self.__products)
            print(ave_prices)
        except ZeroDivisionError:
            return 0


class BaseProduct(ABC):
    # Абстрактный класс родитель для класса Product
    def __init__(self):
        if self.quantity == 0:
            print("Товар с нулевым количеством не может быть добавлен")
            raise ValueError
        super().__init__()


class MixinRepr:
    # Класс Миксин для вывода информации о создаваемом классе
    def __init__(self):
        print(repr(self))
        super().__init__()

    def __repr__(self):
        return (
            f"{self.__class__.__name__}('{self.name}', '{self.description}', "
            f"{self.price}, {self.quantity})"
        )


class Product(BaseProduct, MixinRepr):

    def __init__(self, name, description, price, quantity):
        # Атрибуты экземпляра
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    @classmethod
    def new_product(cls, data):
        return cls(
            name=data["name"],
            description=data["description"],
            price=data["price"],
            quantity=data["quantity"],
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0 and new_price != 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) is type(other):
            return self.quantity * self.__price + other.quantity * other.__price
        raise TypeError


class Smartphone(Product):

    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
