"""Задача 4. Создание класса-фабрики для животных
Создайте базовый класс Animal, который имеет атрибут name, представляющий имя
животного.
Создайте классы Bird, Fish и Mammal, которые наследуются от базового класса Animal и
добавляют дополнительные атрибуты и методы:
Bird имеет атрибут wingspan (размах крыльев) и метод wing_length, который
возвращает длину крыла птицы.
Fish имеет атрибут max_depth (максимальная глубина обитания) и метод depth, который
возвращает категорию глубины рыбы (мелководная, средневодная, глубоководная) в
зависимости от значения max_depth.
Если максимальная глубина обитания рыбы (max_depth) меньше 10, то она относится к
категории "Мелководная рыба".
Если максимальная глубина обитания рыбы больше 100, то она относится к категории
"Глубоководная рыба".
В противном случае, рыба относится к категории "Средневодная рыба".
Mammal имеет атрибут weight (вес) и метод category, который возвращает категорию
млекопитающего (Малявка, Обычный, Гигант) в зависимости от веса. Если вес объекта
меньше 1, то он относится к категории "Малявка".
Если вес объекта больше 200, то он относится к категории "Гигант".
В противном случае, объект относится к категории "Обычный".
Создайте класс-фабрику AnimalFactory, который будет создавать экземпляры животных
разных типов на основе переданного типа и параметров. Класс-фабрика должен иметь
метод create_animal, который принимает следующие аргументы:
animal_type (строка) - тип животного (один из: 'Bird', 'Fish', 'Mammal').
*args - переменное количество аргументов, представляющих параметры для конкретного
типа животного. Количество и типы аргументов могут различаться в зависимости от типа
животного.
Метод create_animal должен создавать и возвращать экземпляр животного заданного
типа с переданными параметрами.
Если animal_type не соответствует 'Bird', 'Fish' или 'Mammal', функция вызовет ValueError с
сообщением 'Недопустимый тип животного'.
Подсказка № 1
Начните с создания базового класса Animal, который содержит атрибут name. Этот
класс будет родительским для других классов животных. Атрибут name будет
передаваться через конструктор __init__.
Подсказка № 2
Создайте классы-наследники Bird, Fish и Mammal. Каждый из этих классов должен
наследоваться от класса Animal и добавлять свои уникальные атрибуты. Например, у
Bird будет атрибут wingspan, у Fish — max_depth, а у Mammal — weight.
Подсказка № 3
В классе Bird создайте метод wing_length, который будет возвращать длину крыла.
Допустим, длина крыла равна половине размаха крыльев (wingspan).
Подсказка № 4
В классе Fish создайте метод depth, который будет возвращать категорию глубины
на основе значения max_depth. Используйте условные конструкции if для проверки
диапазонов глубин."""
class Animal:
    def __init__(self, name):
        self.name = name


class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def wing_length(self):
        return self.wingspan / 2


class Fish(Animal):
    def __init__(self, name, max_depth):
        super().__init__(name)
        self.max_depth = max_depth

    def depth(self):
        if self.max_depth < 10:
            return "Мелководная рыба"
        elif self.max_depth > 100:
            return "Глубоководная рыба"
        else:
            return "Средневодная рыба"


class Mammal(Animal):
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight  

    def category(self):
        if self.weight < 1:
            return "Малявка"
        elif self.weight > 200:
            return "Гигант"
        else:
            return "Обычный"


class AnimalFactory:
    @staticmethod
    def create_animal(animal_type, *args):
        if animal_type == "Bird":
            return Bird(*args)
        elif animal_type == "Fish":
            return Fish(*args)
        elif animal_type == "Mammal":
            return Mammal(*args)
        else:
            raise ValueError("Недопустимый тип животного")



if __name__ == "__main__":
    factory = AnimalFactory()

    bird = factory.create_animal("Bird", "Орел", 2.4)
    print(f"Птица: {bird.name}, размах крыльев: {bird.wingspan}, длина крыла: {bird.wing_length()}")

    fish = factory.create_animal("Fish", "Акула", 150)
    print(f"Рыба: {fish.name}, максимальная глубина: {fish.max_depth}, категория: {fish.depth()}")

    mammal = factory.create_animal("Mammal", "Слон", 5000)
    print(f"Млекопитающее: {mammal.name}, вес: {mammal.weight}, категория: {mammal.category()}")
