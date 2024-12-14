# Задача 3. Счётчик
# Реализуйте декоратор counter, считающий и выводящий количество вызовов
# декорируемой функции.
# Для решения задачи нельзя использовать операторы global и nonlocal.
# Пример: Из файла products.json нужно создать products.csv.
# Подсказка № 1
# Создайте атрибут обертки для хранения счетчика. Добавьте переменную `count`
# непосредственно в функцию-обертку, чтобы она могла отслеживать количество
# вызовов без использования глобальных переменных.
# Подсказка № 2
# Инициализируйте счетчик по умолчанию. Перед возвратом обертки, установите
# `wrapper.count = 0`, чтобы счетчик начинал отсчет с нуля при каждом новом
# декорировании функции.
# Подсказка № 3
# Увеличивайте счетчик при каждом вызове обертки. Внутри функции-обертки
# увеличивайте значение атрибута `wrapper.count` на единицу каждый раз, когда
# вызывается декорируемая функция.
# Подсказка № 4
# Используйте `functools.wraps` для сохранения метаданных функции. К применению
# декоратора добавьте `@wraps(func)` к функции-обертке, чтобы сохранить
# оригинальные имя и документацию декорируемой функции.
# Подсказка № 5
# Выводите количество вызовов функции после ее выполнения. После вызова
# декорируемой функции в обертке добавьте вывод, который покажет, сколько раз
# функция была вызвана до текущего момента.


from functools import wraps
from typing import Callable, Any, Optional
def counter(func: Callable) -> Callable:
    """
    Декоратор для подсчета количества вызовов функции.
    :param func: Декорируемая функция.
    :return: Обертка функции с подсчетом вызовов.
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        """
        Функция-обертка для увеличения и вывода счётчика вызовов
        функции.
        :param args: Позиционные аргументы декорируемой функции.
        :param kwargs: Именованные аргументы декорируемой функции.
        :return: Результат вызова декорируемой функции.
        """
        wrapper.count += 1 # Увеличиваем счетчик вызовов на единицу.
        result = func(*args, **kwargs) # Вызываем оригинальную функцию.
        print(f"Функцию '{func.__name__}' вызвали {wrapper.count} раз")
        # Выводим количество вызовов.
        return result # Возвращаем результат вызова оригинальной
    wrapper.count = 0 # Инициализируем счетчик вызовов.
    return wrapper # Возвращаем обертку.

@counter
def greeting(name: str, age: Optional[int] = None) -> str:
    """
    Приветствие с возрастом и именем.
    :param name: Имя человека.
    :param age: Возраст человека (по умолчанию None).
    :return: Строка с приветствием.
    """
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растешь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)
    
@counter
def greeting2(name: str) -> None:
    """
    Приветствие с именем. Вывод в консоль.
    :param name: Имя человека.
    :return: None.
    """
    print(f'Привет, {name}!')

def main() -> None:
    """
    Основная функция для запуска.
    :return: None.
    """
    greeting("Том") # Вызов функции greeting с одним аргументом.
    greeting("Миша", age=100) # Вызов функции greeting с двумя аргументами.
    greeting2("Маша") # Вызов функции greeting2.
    greeting(name="Катя", age=16) # Вызов функции greeting с именем и возрастом.

main() # Запуск основной функции.