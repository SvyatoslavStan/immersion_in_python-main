def generate_pit(N):
    for i in range(N):
        left_part = ''.join(str(N - j) for j in range(i + 1))
        dots = '.' * (2 * (N - i - 1))
        right_part = ''.join(str(N - j) for j in range(i, -1, -1))
        print(left_part + dots + right_part)

N = int(input("Введите глубину ямы: "))
generate_pit(N)
