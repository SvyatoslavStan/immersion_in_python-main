# Задача 4. Агрегирование данных из CSV файла
# Напишите скрипт, который считывает данные из CSV файла, содержащего
# информацию о продажах (название продукта, количество, цена за единицу), и
# подсчитывает общую выручку для каждого продукта. Итог должен быть сохранён в
# новом CSV файле.
# Пример: Из файла sales.csv нужно создать файл total_sales.csv, где для каждого
# продукта будет указана общая выручка.
# Подсказка № 1
# Используйте csv.DictReader для чтения данных из исходного CSV файла.
# csv.DictReader позволяет читать строки CSV файла как словари, где ключи
# соответствуют заголовкам столбцов.
# Подсказка № 2
# Создайте словарь для хранения выручки по каждому продукту. Используйте продукт в
# качестве ключа и выручку в качестве значения. Убедитесь, что добавляете выручку при
# встрече одинакового продукта.
# Подсказка № 3
# Используйте csv.DictWriter для записи данных в новый CSV файл. Запишите итоговые
# данные в новый файл, указывая заголовки столбцов и записывая итоговую выручку
# для каждого продукта.
# Подсказка № 4
# Преобразуйте данные в числовые типы для корректного вычисления выручки.
# Убедитесь, что данные из CSV преобразованы в целые или вещественные числа,
# чтобы корректно производить арифметические операции.

import csv
import os

def read_sales_data(file_path):
    sales_data = []
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                sales_data.append(row)
        return sales_data
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []
    except Exception as e:
        print(f"Произошла ошибка при чтении файла {file_path}: {e}")
        return []

def aggregate_sales(sales_data):
    total_sales = {}
    for entry in sales_data:
        product = entry.get('product')
        quantity = entry.get('quantity')
        price = entry.get('price')
        try:
            quantity = int(quantity)
            price = float(price)
        except ValueError:
            print(f"Некорректные данные для продукта '{product}': quantity='{quantity}', price='{price}'. Пропуск записи.")
            continue

        revenue = quantity * price

        if product in total_sales:
            total_sales[product] += revenue
        else:
            total_sales[product] = revenue

    return total_sales

def write_total_sales(total_sales, output_file):
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['product', 'total_revenue']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for product, revenue in total_sales.items():
                writer.writerow({
                    'product': product,
                    'total_revenue': f"{revenue:.2f}"
                })
        print(f"Общая выручка успешно записана в {output_file}.")
    except Exception as e:
        print(f"Произошла ошибка при записи в файл {output_file}: {e}")

def main():

    script_dir = os.path.dirname(os.path.abspath(__file__))
    sales_file = os.path.join(script_dir, 'sales.csv')
    total_sales_file = os.path.join(script_dir, 'total_sales.csv')
    sales_data = read_sales_data(sales_file)

    if not sales_data:
        print("Нет данных для обработки. Завершение программы.")
        return

    total_sales = aggregate_sales(sales_data)

    if not total_sales:
        print("Нет агрегированных данных для записи. Завершение программы.")
        return

    write_total_sales(total_sales, total_sales_file)

if __name__ == "__main__":
    main()
