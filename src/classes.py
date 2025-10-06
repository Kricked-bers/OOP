class Category:
    # Атрибуты класса
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        # Атрибуты экземпляра
        self.name = name
        self.description = description
        self.__products = products

        # Обновляем атрибуты класса
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, new_product):
        Category.product_count += 1
        self.__products.append(new_product)

    @property
    def products(self):
        product_list = [
            f"{i.name}, {i.price} руб. Остаток: {i.quantity} шт."
            for i in self.__products
        ]
        return product_list

    @property
    def get_list_products(self):
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


product_5 = Product("Мышь", "Беспроводная мышь", 25.50, 50)
product_5.price = -5
print(product_5.price)
