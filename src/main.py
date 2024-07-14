from abc import ABC, abstractmethod


class LoggingMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print(f"Создан объект {self.__class__.__name__}({repr(self)})")


class Category(LoggingMixin):
    """Класс для представления категорий"""

    total_amount_category = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = set(products)
        self.unique_products = len(self.__products)
        Category.total_amount_category += 1
        super().__init__()

    def __repr__(self):
        return f"{self.__class__.__name__}{self.name}, {self.description}, {self.__products}, "

    def __str__(self):
        return f"'{self.name}', '{self.description}',{self.products}"

    def __len__(self):
        return sum(product.amount for product in self.__products)

    def add_product(self, product):
        """Добавление продукта в категорию, добавляет только наследников продукта"""
        if isinstance(product, Product) and issubclass(type(product), Product):
            self.__products.add(product)
        else:
            raise TypeError("Можно добавлять только экземпляры Product или его подклассы.")

    @property
    def products(self):
        """Геттер для вывода списка товаров в заданном формате"""
        product_list = []
        for product in self.__products:
            product_list.append(f"{product.name}, {product.price} руб. Остаток: {product.amount} шт.")
        return product_list


class AllProducts(ABC):
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def price(self):
        pass

    @abstractmethod
    def amount(self):
        pass


class Product(AllProducts, LoggingMixin):
    """Класс для представления продукта"""

    def __init__(self, name: str, description, price: float, amount: int):
        self._name = name
        self.description = description
        self._price = price
        self._amount = amount
        super().__init__()

    def __repr__(self):
        return f"{self.__class__.__name__},{self.name}, {self.description}, {self.price}, {self.amount}"

    def __str__(self):
        return f"'{self.name}', '{self.description}', {self.price}, {self.amount}"

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
        """Метод складывающий одинаковые классы продуктов"""
        if isinstance(other, type(self)):
            return self.price * self.amount + other.price * other.amount
        raise TypeError("Невозможно добавить товар разных типов")

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


class SmartPhone(Product, LoggingMixin):
    """Родительский класс берущий основные параметры и добавляющий новые"""

    def __init__(self, name, description, price, amount, perfomance, model, memory, color):
        self.perfomance = perfomance
        self.model = model
        self.color = color
        self.memory = memory
        super().__init__(name, description, price, amount)


class GrassLawn(Product, LoggingMixin):
    """Родительский класс берущий основные параметры и добавляющий новые"""

    def __init__(self, name, description, price, amount, country_made, period_height, color):
        self.country_made = country_made
        self.period_height = period_height
        self.color = color
        super().__init__(name, description, price, amount)


if __name__ == "__main__":
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

    phone = SmartPhone("iphone", "телефон с ios системой", 10000, 10, 100, "XR", "128 GB", "Красный")

    Grass = GrassLawn("vivo", "трава из италии", 100, 30, "Италия", "10 дней", "Зеленая")

    # print(Grass)
    # print(Grass.period_height)
    # print(Grass.color)
    # print(Grass.country_made)

    # print(phone)
    # print(phone.model)
    # print(phone.memory)
    # print(phone.perfomance)
    # print(phone.color)
