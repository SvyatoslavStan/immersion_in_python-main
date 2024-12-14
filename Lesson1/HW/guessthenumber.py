def guess_number(lower_bound, upper_bound):
    
    count = 1
    while True:
        i_suppose = (lower_bound + upper_bound) // 2
        answer = interface(i_suppose, count)
        if answer == 1:
            print(f"Угадал! С {count} попытки. Твое число: {i_suppose}")
            break
        elif answer == 2:
            lower_bound = i_suppose + 1
        elif answer == 3:
            upper_bound = i_suppose - 1
        count += 1

def interface(i_suppose, count):
    print(f"Попытка {count}: Загаданное число {i_suppose}:\n1 — равно\n2 — больше\n3 — меньше\n")
    while True:
        try:
            answer = int(input("Твой ответ: "))
            if answer in [1, 2, 3]:
                return answer
            else:
                print("Введите 1, 2 или 3.")
        except ValueError:
            print("Введите число.")

lower_bound = 1
upper_bound = 100
guess_number(lower_bound, upper_bound)
