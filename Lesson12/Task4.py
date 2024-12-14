class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __setattr__(self, name, value):
        if name == "price":
            if not (isinstance(value, (int, float)) and value > 0):
                raise ValueError("Цена должна быть положительным числом больше нуля")
        elif name == "quantity":
            if not (isinstance(value, int) and value >= 0):
                raise ValueError("Количество должно быть неотрицательным целым числом")
        super().__setattr__(name, value)

    def __str__(self):
        return f"Товар: {self.name}, Цена: {self.price}, Количество: {self.quantity}"

    def total_cost(self):
        return self.price * self.quantity

    def add_stock(self, amount):
        if not (isinstance(amount, int) and amount > 0):
            raise ValueError("Добавляемое количество должно быть положительным целым числом")
        self.quantity += amount

    def sell(self, amount):
        if not (isinstance(amount, int) and amount > 0):
            raise ValueError("Количество для продажи должно быть положительным целым числом")
        if amount > self.quantity:
            raise ValueError("Нельзя продать больше, чем есть в наличии")
        self.quantity -= amount

try:
    apple = Product("Яблоко", 50.0, 100)
    print(apple)

    banana = Product("Банан", 25.5, 200)
    print(banana)

    orange = Product("Апельсин", 40, 150)
    print(orange)

    print(f"Общая стоимость {apple.name}: {apple.total_cost()}")

    apple.add_stock(50)
    print(f"Количество {apple.name} после пополнения: {apple.quantity}")

    apple.sell(30)
    print(f"Количество {apple.name} после продажи: {apple.quantity}")

    banana.price = 30
    print(f"Новая цена {banana.name}: {banana.price}")

    orange.price = -10

except ValueError as e:
    print(f"Ошибка: {e}")
