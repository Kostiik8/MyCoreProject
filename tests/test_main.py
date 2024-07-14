import pytest

from src.main import Category, Product, SmartPhone, GrassLawn


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


@pytest.mark.parametrize(
    "new_product, expected_products",
    [
        (
            Product("Яблоко", "Фрукт", 50, 20),
            {
                "Банан, 15 руб. Остаток: 6 шт.",
                "Груша, 10 руб. Остаток: 5 шт.",
                "Яблоко, 50 руб. Остаток: 20 шт.",
            },
        ),
        (
            SmartPhone("iphone", "телефон с ios системой", 10000, 10, 100, "XR", "128 GB", "Красный"),
            {
                "Банан, 15 руб. Остаток: 6 шт.",
                "Груша, 10 руб. Остаток: 5 шт.",
                "iphone, 10000 руб. Остаток: 10 шт.",
            },
        ),
        (
            GrassLawn("vivo", "трава из италии", 100, 30, "Италия", "10 дней", "Зеленая"),
            {
                "Банан, 15 руб. Остаток: 6 шт.",
                "Груша, 10 руб. Остаток: 5 шт.",
                "vivo, 100 руб. Остаток: 30 шт.",
            },
        ),
    ],
)
def test_add_product(test_category, new_product, expected_products):
    """Тест проверяет что не добавляются другие категории в категории продуктов"""
    test_category.add_product(new_product)
    assert set(test_category.products) == expected_products


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
    assert Category.total_amount_category == 5


@pytest.fixture
def test_product():
    product1 = Product("Банан", "Фрукт", 15, 6)
    return product1


def test_init_2(test_product):
    assert test_product.name == "Банан"
    assert test_product.description == "Фрукт"
    assert test_product.price == 15
    assert test_product.amount == 6


@pytest.fixture
def test_product_sum_rub(test_category):
    product4 = Product("Арбуз", "ягода", 1000, 3)
    product5 = Product("Дыня", "фрукт", 1500, 2)
    combined_product = product4 + product5

    assert combined_product.name == "Арбуз и Дыня"
    assert combined_product.description == "ягода и фрукт"
    assert combined_product.price == 1000 * 3 + 1500 * 2
    assert combined_product.amount == 5
    assert str(combined_product) == "Арбуз и Дыня, 6000 руб. Остаток: 5 шт."
    assert len(combined_product.products) == 4


@pytest.fixture
def category(test_category):
    return Product("Арбуз", "ягода", 1000, 3)


def test_create_category(category):
    assert category.name == "Арбуз"
    assert category.description == "ягода"
    assert len(category) == 25
    assert str(category) == "'Арбуз', 'ягода', 1000, 3"


@pytest.fixture
def test_news_category(test_category):
    return SmartPhone("iphone", "телефон с ios системой", 10000, 10, 100, "XR", "128 GB", "Красный")


def test_add_news(test_news_category):
    assert test_news_category.name == "iphone"
    assert test_news_category.description == "телефон с ios системой"
    assert test_news_category.price == 10000
    assert test_news_category.amount == 10
    assert test_news_category.perfomance == 100
    assert test_news_category.model == "XR"
    assert test_news_category.memory == "128 GB"
    assert test_news_category.color == "Красный"


def test_add_different_types():
    """Создаем экземпляр класса Product и экземпляр другого типа"""
    product1 = Product("Шоколад", "Шоколадный батончик", 50, 5)
    other_object = "some_string"

    with pytest.raises(TypeError):
        product1 + other_object
