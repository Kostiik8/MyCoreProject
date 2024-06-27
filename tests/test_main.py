import pytest

from src.main import Category, Product


@pytest.fixture
def test_category():
    product1 = Product("Банан", "фрукт", 15, 6)
    product2 = Product("Груша", "фрукты", 10, 5)
    category = Category("Фрукты", "Различные свежие фрукты", [product1, product2, product2])
    return category


def test_init(test_category):
    assert test_category.name == "Фрукты"
    assert test_category.description == "Различные свежие фрукты"
    assert set(test_category.products) == {"Банан, 15 руб. Остаток: 6 шт.", "Груша, 10 руб. Остаток: 5 шт."}


def test_add_product(test_category):
    new_product = Product("Яблоко", "Фрукт", 50, 20)
    test_category.add_product(new_product)
    assert set(test_category.products) == {
        "Банан, 15 руб. Остаток: 6 шт.",
        "Груша, 10 руб. Остаток: 5 шт.",
        "Яблоко, 50 руб. Остаток: 20 шт.",
    }


def test_set_price():
    product = Product("Яблоко", "фрукт", 0, 10)
    product.price = 20
    assert product.price == 20


def test_set_amount():
    product = Product("Яблоко", "фрукт", 20, 10)
    product.amount = 15
    assert product.amount == 15


def test_class(test_category):
    assert test_category.unique_products == 2
    assert Category.total_amount_category == 4


@pytest.fixture
def test_product():
    product1 = Product("Банан", "Фрукт", 15, 6)
    return product1


def test_init_2(test_product):
    assert test_product.name == "Банан"
    assert test_product.description == "Фрукт"
    assert test_product.price == 15
    assert test_product.amount == 6
