# Задача 4. Сумма и произведение дробей
# Программа принимает две строки вида "a/b" - дробь с числителем и
# знаменателем. Возвращает сумму и произведение дробей. Для проверки
# используется модуль fractions.
# Подсказка № 1
# Используйте метод split('/') для разделения строки на числитель и знаменатель.
# Преобразуйте полученные части в целые числа с помощью функции map(int, ...).
# Подсказка № 2
# Импортируйте класс Fraction из модуля fractions, чтобы легко работать с
# дробями. Создайте объекты Fraction, передав числитель и знаменатель.
# Подсказка № 3
# Используйте операторы + и * для нахождения суммы и произведения дробей
# соответственно. Класс Fraction автоматически упрощает дроби и выполняет
# операции корректно.

from fractions import Fraction

try:
    fraction1_str = input("Введите первую дробь (в формате a/b): ")
    fraction2_str = input("Введите вторую дробь (в формате a/b): ")

    numerator1, denominator1 = map(int, fraction1_str.split('/'))
    numerator2, denominator2 = map(int, fraction2_str.split('/'))

    fraction1 = Fraction(numerator1, denominator1)
    fraction2 = Fraction(numerator2, denominator2)

    sum_result = fraction1 + fraction2
    product_result = fraction1 * fraction2

    print(f"Сумма дробей: {sum_result}")
    print(f"Произведение дробей: {product_result}")

except ValueError:
    print("Некорректный ввод. Пожалуйста, используйте формат a/b для дробей.")
