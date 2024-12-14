# Задание №6
# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

def atm_program():
    balance = 0
    total_operations = 0
    wealth_tax_threshold = 5_000_000

    while True:
        print(f"Текущий баланс: {balance} у.е.")
        action = input("Выберите действие (пополнить/снять/выйти): ").lower()

        if action == "выйти":
            print("Спасибо за использование нашего банкомата!")
            break
        elif action == "пополнить":
            deposit = int(input("Введите сумму для пополнения (кратную 50): "))
            if deposit % 50 != 0:
                print("Сумма должна быть кратной 50.")
                continue
            balance += deposit
        elif action == "снять":
            withdrawal = int(input("Введите сумму для снятия (кратную 50): "))
            if withdrawal % 50 != 0:
                print("Сумма должна быть кратной 50.")
                continue
            if withdrawal > balance:
                print("Недостаточно средств на счете.")
                continue
            withdrawal_fee = max(30, min(600, withdrawal * 0.015))
            balance -= withdrawal + withdrawal_fee
        else:
            print("Некорректное действие. Пожалуйста, выберите пополнить, снять или выйти.")

        total_operations += 1
        if total_operations % 3 == 0:
            balance *= 0.97 

        if balance >= wealth_tax_threshold:
            wealth_tax = balance * 0.1
            balance -= wealth_tax
            print(f"Применен налог на богатство: {wealth_tax:.2f} у.е.")

    print(f"Итоговый баланс: {balance} у.е.")


atm_program()

