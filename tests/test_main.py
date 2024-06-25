import pytest

from src.main import Category, Product


@pytest.fixture
def test_category():
    return Category("Фрукты", "Различные свежие фрукты", ["Банан", "Груша", "Груша"])


def test_init(test_category):
    assert test_category.name == "Фрукты"
    assert test_category.description == "Различные свежие фрукты"
    assert test_category.products == {"Банан", "Груша"}
    assert test_category.unique_products == 2
    assert test_category.total_amount_category == 1


@pytest.fixture
def test_product():
    return Product("Яблоко", "Фрукт", 100.1, 10)


def test_init_2(test_product):
    assert test_product.name == "Яблоко"
    assert test_product.description == "Фрукт"
    assert test_product.price == 100.1
    assert test_product.amount == 10
