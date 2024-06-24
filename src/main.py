class Category:
    """Класс для представления категорий"""
    total_amount_category = 0
    unique_products = set()

    def __init__(self, name: str, description: str, products: str):
        self.name = name
        self.description = description
        self.products = products


class Product:
    """Класс для представления продукта"""
    def __init__(self, name: str, description: str, price: float, amount: float):
        self.name = name
        self.description = description
        self.price = price
        self.amount = amount
