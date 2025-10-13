from itertools import product

import pytest

from src.classes import Category, Product


class TestProduct:
    def test_product_creation(self):
        """Тест создания продукта и проверки его атрибутов"""
        product = Product("Ноутбук", "Мощный игровой ноутбук", 1500.00, 10)

        assert product.name == "Ноутбук"
        assert product.description == "Мощный игровой ноутбук"
        assert product.price == 1500.00
        assert product.quantity == 10

    def test_product_default_values(self):
        """Тест создания продукта с разными значениями"""
        product = Product("Мышь", "Беспроводная мышь", 25.50, 50)

        assert product.name == "Мышь"
        assert product.description == "Беспроводная мышь"
        assert product.price == 25.50
        assert product.quantity == 50

    def test_new_product(self):
        product_5 = Product("Мышь", "Беспроводная мышь", 25.50, 50)
        assert product_5.price == 25.50
        product_6 = product_5.new_product(
            {"name": "Мышка", "description": "Проводная мышь", "price": 15, "quantity": 50})
        assert product_6.price == 15

    def test_new_price(self):
        product_7 = Product("Мышь", "Беспроводная мышь", 25.50, 50)
        product_7.price = 500
        assert product_7.price == 500


class TestCategory:
    def test_category_creation(self):
        """Тест создания категории и проверки ее атрибутов"""
        # Сбросим счетчики перед тестом
        Category.category_count = 0
        Category.product_count = 0

        product = Product("Ноутбук", "Мощный игровой ноутбук", 1500.00, 10)
        category = Category("Электроника", "Электронные устройства", [product])

        assert category.name == "Электроника"
        assert category.description == "Электронные устройства"
        assert len(category.products) == 1
        assert category.get_list_products[0].name == "Ноутбук"

    def test_category_counters(self):
        """Тест обновления счетчиков категорий и продуктов"""
        # Сбросим счетчики перед тестом
        Category.category_count = 0
        Category.product_count = 0

        # Создаем несколько продуктов и категорий
        product1 = Product("Ноутбук", "Мощный игровой ноутбук", 1500.00, 10)
        product2 = Product("Мышь", "Беспроводная мышь", 25.50, 50)

        category1 = Category("Электроника", "Электронные устройства", [product1, product2])

        # Проверяем счетчики после создания первой категории
        assert Category.category_count == 1

        # Создаем еще одну категорию
        product3 = Product("Книга", "Программирование на Python", 35.00, 20)
        category2 = Category("Книги", "Книги и учебники", [product3])

    def test_empty_category(self):
        """Тест создания категории без продуктов"""
        # Сбросим счетчики перед тестом
        Category.categories_count = 0
        Category.product_count = 0

        category = Category("Пустая категория", "Нет продуктов", [])

        assert category.name == "Пустая категория"
        assert category.description == "Нет продуктов"
        assert len(category.products) == 0
        assert Category.categories_count == 0

    def test_add_product_category(self):
        cat_empty = Category("Отечественная литература", "Толстой", [])
        product4 = Product("Книга", "Война и мир", 45, 20)
        cat_empty.add_product(product4)
        assert cat_empty.products == ["Книга, 45 руб. Остаток: 20 шт."]
