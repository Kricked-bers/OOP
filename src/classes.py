class Category:
    # Атрибуты класса
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        # Атрибуты экземпляра
        self.name = name
        self.description = description
        self.__products = products
        self.__allowed_type = type(products[0]) if products else None

    def add_product(self, new_product):
        if self.__products and self.__allowed_type:
            if isinstance(new_product, self.__allowed_type):
                self.__products.append(new_product)
            else:
                raise TypeError
        else:
            # Если категория пустая, устанавливаем разрешенный
            # тип и добавляем продукт
            self.__allowed_type = type(new_product)
            self.__products.append(new_product)

    def __str__(self):
        return (
            f"{self.name}, количество продуктов: "
            f"{sum([i.quantity for i in self.__products])} шт."
        )

    @property
    def products(self):
        return self.__products


class Product:
    def __init__(self, name, description, price, quantity):
        # Атрибуты экземпляра
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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
        if isinstance(other, self.__class__):
            return (self.quantity * self.__price +
                    other.quantity * other.__price)
        raise TypeError


class Smartphone(Product):

    def __init__(
            self, name, description, price, quantity, efficiency,
            model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(
            self, name, description, price, quantity,
            country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
