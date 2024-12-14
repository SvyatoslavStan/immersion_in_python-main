def primenumbers(quantity):
    numbers = []
    while quantity != 0:
        number = float(input("Введите число: "))
        numbers.append(number)
        quantity -= 1
    print("Введенные числа: ", numbers)
    
    count = isprime(numbers)
    print(f"Количество простых чисел: {count}")

def isprime(numbers):
    count = 0
    for number in numbers:
        if number < 2:
            continue
        is_prime = True
        for i in range(2, int(number**0.5) + 1):
            if number % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
    return count


quantity = int(input("Введите количество чисел: "))
primenumbers(quantity)
