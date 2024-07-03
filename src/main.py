class Category:
    """Класс для представления категорий"""

    total_amount_category = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = set(products)
        self.unique_products = len(self.__products)
        Category.total_amount_category += 1

    def __repr__(self):
        return f"{self.__class__.__name__}{self.name}, {self.description}, {self.__products}, "

    def __str__(self):
        return f"{self.name}, количество продуктов: {len(self)} шт."

    def __len__(self):
        return sum(product.amount for product in self.__products)

    def add_product(self, product):
        """Добавление продукта в категорию."""
        self.__products.add(product)
        self.unique_products = len(self.__products)

    @property
    def products(self):
        """Геттер для вывода списка товаров в заданном формате"""
        product_list = []
        for product in self.__products:
            product_list.append(f"{product.name}, {product.price} руб. Остаток: {product.amount} шт.")
        return product_list


class Product:
    """Класс для представления продукта"""

    def __init__(self, name: str, description, price: float, amount: int):
        self._name = name
        self.description = description
        self._price = price
        self._amount = amount

    def __repr__(self):
        return f"{self.__class__.__name__},{self.name}, {self.description}, {self.price}, {self.amount}"

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.amount} шт."

    def __len__(self):
        return len(str(self))

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Некорректное цена")
        else:
            self._price = value

    def __add__(self, other):
        return Product(
            f"{self.name} и {other.name}",
            f"{self.description} и {other.description}",
            self.price * self.amount + other.price * other.amount,
            self.amount + other.amount,
        )

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if value <= 0:
            print("Некорректное количество")
        else:
            self._amount = value

    @amount.deleter
    def amount(self):
        del self._amount

    @classmethod
    def create_product(cls, name, description, price, amount):
        """Метод, который создает товар и возвращает объект"""
        return cls(name, description, price, amount)


product1 = Product("Банан", "фрукт", 15, 6)
product2 = Product("Груша", "фрукты", 10, 5)
product3 = Product("Яблоко", "фрукт", 20, 1)
product4 = Product("Киви", "фрукт", 100, 10)
product5 = Product("Личи", "фрукт", 150, 15)

product6 = product4 + product5
print(product6)
category = Category("Фрукты", "Различные свежие фрукты", [product1, product2, product2])

category.add_product(product3)
print(category)
for product in category.products:
    print(product)
