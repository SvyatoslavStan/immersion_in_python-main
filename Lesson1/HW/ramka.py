height = int(input("Введите высоту: "))
width = int(input("Введите ширину: "))

print("+" + "-" * width + "+")

for i in range(height):
    print("|" + " " * width + "|")

print("+" + "-" * width + "+")