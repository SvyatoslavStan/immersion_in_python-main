# Задание 1. Квадраты чисел
# Пользователь вводит число N. Напишите программу, которая генерирует
# последовательность из квадратов чисел от 1 до N (1 ** 2, 2 ** 2, 3 ** 2 и так
# далее). Реализацию напишите двумя способами: функция-генератор и
# генераторное выражение.
# Подсказка № 1
# Создайте функцию-генератор generator_function, которая принимает одно целое
# число n и генерирует квадраты чисел от 1 до n. Для этого используйте ключевое слово
# yield, чтобы возвращать каждый квадрат по мере необходимости.
# Подсказка № 2
# Внутри функции-генератора generator_function организуйте цикл, который будет
# итерироваться по числам от 1 до n включительно. На каждой итерации с помощью
# yield возвращайте квадрат текущего числа. Это позволяет функции "запоминать"
# своё состояние и продолжать выполнение с места остановки при следующем вызове.
# Подсказка № 3
# Реализуйте функцию-генератор, которое создайте генераторное выражение для
# генерации квадратов чисел от 1 до n. Генераторное выражение имеет более
# компактный синтаксис и создаётся внутри круглых скобок. Выведите сгенерированные
# значения с помощью цикла for.
# 



# Способ 1
def generator_function(n):
    for i in range(1, n + 1):
        yield i ** 2

N = int(input("Введите число N: "))

print("Квадраты чисел (функция-генератор):")
for square in generator_function(N):
    print(square, end=" ")

#  Способ2

squares_generator = (i ** 2 for i in range(1, N + 1))

print("\nКвадраты чисел (генераторное выражение):")
for square in squares_generator:
    print(square, end=" ")
