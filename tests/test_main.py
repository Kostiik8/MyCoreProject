import pytest

from src.main import Category, Product


@pytest.fixture
def test_category():
    category1 = Category("Фрукты", "Различные свежие фрукты", ["Банан", "Груша", "Груша"])
    category2 = Category("Овощи", "Различные свежие овощи", ["Морковь", "Капуста"])
    return category1


def test_init(test_category):
    assert test_category.name == "Фрукты"
    assert test_category.description == "Различные свежие фрукты"
    assert test_category.products == {"Банан", "Груша"}
    assert test_category.unique_products == 2
    assert Category.total_amount_category == 2


@pytest.fixture
def test_product():
    return Product("Яблоко", "Фрукт", 100.1, 10)


def test_init_2(test_product):
    assert test_product.name == "Яблоко"
    assert test_product.description == "Фрукт"
    assert test_product.price == 100.1
    assert test_product.amount == 10
