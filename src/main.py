class Category:
    """Класс для представления категорий"""

    unique_products = 0
    total_amount_category = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = set(products)
        Category.total_amount_category += 1
        Category.unique_products = len(set(self.products))


class Product:
    """Класс для представления продукта"""

    def __init__(self, name: str, description: str, price: float, amount: float):
        self.name = name
        self.description = description
        self.price = price
        self.amount = amount


cat1 = Category("Фрукты", "Различные свежие фрукты", ["Банан", "Груша", "Груша"])
cat2 = Category("Овощи", "Различные  Овощи", ["Морковь", "Морковь", "Свекла"])
print(Category.total_amount_category)
print(Category.unique_products)
