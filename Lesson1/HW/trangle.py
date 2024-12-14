def triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print("Треугольник существует")
        if a == b == c:
            print("Треугольник равносторонний")
        elif a == b or a == c or b == c:
            print("Треугольник равнобедренный")
        else:
            print("Треугольник разносторонний")
    else:
        print("Треугольника не существует")


a = float(input("Введите сторону а: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))

triangle(a, b, c)