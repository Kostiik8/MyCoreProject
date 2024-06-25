class Category:
    """Класс для представления категорий"""

    total_amount_category = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = set(products)
        self.unique_products = len(self.products)
        Category.total_amount_category += 1


class Product:
    """Класс для представления продукта"""

    def __init__(self, name: str, description: str, price: float, amount: float):
        self.name = name
        self.description = description
        self.price = price
        self.amount = amount
