# Задание 1. Отцы, матери и дети.
# Вася совсем заскучал на работе и решил побаловаться с кодом проекта. Он
# Реализуйте два класса: «Родитель» и «Ребёнок». У родителя есть:
# ● имя,
# ● возраст,
# ● список детей.
# И он может:
# ● сообщить информацию о себе,
# ● успокоить ребёнка,
# ● покормить ребёнка.
# У ребёнка есть:
# ● имя,
# ● возраст (должен быть меньше возраста родителя хотя бы на 16 лет),
# ● состояние спокойствия,
# ● состояние голода.
# Реализация состояний — на ваше усмотрение. Это может быть и простой «флаг»,
# и словарь состояний, и что-то поинтереснее.
# Подсказка № 1
# Используйте проверку на разницу в возрасте при добавлении ребёнка в список детей.
# Это поможет убедиться, что разница в возрасте между родителем и ребёнком
# составляет хотя бы 16 лет.
# Подсказка № 2
# Реализуйте методы feed() и calm() в классе Parent, чтобы они изменяли
# соответствующие состояния ребёнка. Например, состояние голода можно представить
# как логическое значение (True/False) или строку («голоден»/«сыт»).
# Подсказка № 3
# Используйте методы __str__() или __repr__() в классах Parent и Child, чтобы
# предоставить более удобный вывод информации о них. Это улучшит читаемость кода,
# когда объекты классов будут выводиться в консоль.
# Подсказка № 4
# Добавьте метод для вывода информации о детях родителя. Это позволит родителю
# предоставить информацию о всех своих детях в одном месте, что упростит управление
# объектами.

class Parent:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.children = []

    
    def info(self):
        """информация о родителе"""
        print(f"Мое имя {self.name}, мне {self.age} лет")


    def add_child(self, child):
        """Добавить ребенка если разница в возрасте более 16 лет"""
        if self.age - child.age >= 16:
            self.children.append(child)
            print(f"Ребёнок {child.name} добавлен к {self.name}.")
        else:
            print(f"Ребёнок {child.name} не добавлен к {self.name}, так как разница в возрасте слишком мала.")


    def feed(self, child):
        """Кормит ребёнка, изменяя его состояние голода"""
        if child in self.children:
            child.hunger = False
            print(f"{self.name} покормил(а) {child.name}.")
        else:
            print(f"{child.name} не является ребёнком {self.name}.")

    def calm(self, child):
        """Успокаивает ребёнка, изменяя его состояние спокойствия"""
        if child in self.children:
            child.calmmness = True
            print(f"{self.name} успокоил(а) {child.name}.")
        else:
            print(f"{child.name} не является ребёнком {self.name}.")

    def list_children(self):
        """Выводит информацию обо всех детях родителя"""
        if self.children:
            print(f"У {self.name} есть следующие дети:")
            for child in self.children:
                print(f" - {child}")
        else:
            print(f"У {self.name} нет детей.")

class Child:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.calmness = True
        self.hunger = True
        

    def get_status(self):
        """Сообщает текущее состояние ребёнка"""
        calm_status = "спокоен" if self.calmness else "не спокоен"
        hungry_status = "сыт" if not self.hunger else "голоден"
        print(f"Ребёнок {self.name} {calm_status} и {hungry_status}.")

    def __str__(self):
        """Представление объекта ребёнка в виде строки"""
        return f"Ребёнок {self.name}, {self.age} лет"

        

# Создание объектов
parent = Parent("Иван", 40)
child1 = Child("Анна", 20)
child2 = Child("Петя", 10)
child3 = Child("Маша", 3)
# Добавление детей к родителю
for child in [child1, child2, child3]:
    parent.add_child(child)
# Вывод информации о родителе и его детях
parent.info()
parent.list_children()
# Родитель кормит и успокаивает детей
for child in parent.children:
    parent.feed(child)
    parent.calm(child)
    child.get_status()
