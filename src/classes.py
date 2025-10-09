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
        self.__products.append(new_product)

    def __str__(self):
        return (f"{self.name}, количество продуктов: "
                f"{sum([i.quantity for i in self.__products])} шт.")

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
        if not isinstance(other, Product):
            return f"Ожидался Product, а получен {type(other).__name__}"
        return self.quantity * self.__price + other.quantity * other.__price
