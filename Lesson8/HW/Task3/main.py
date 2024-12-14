# Задача 3. Агрегирование данных из CSV файла
# Напишите скрипт, который считывает данные из JSON файла и сохраняет их в CSV
# файл. JSON файл содержит данные о продуктах (название, цена, количество на
# складе). В CSV файле каждая строка должна соответствовать одному продукту.
# Пример: Из файла products.json нужно создать products.csv.
# Подсказка № 1
# Используйте json.load() для чтения данных из JSON файла. Функция json.load()
# позволяет загрузить данные из JSON файла в виде Python объекта, например, списка
# словарей.
# Подсказка № 2
# Используйте csv.DictWriter для записи данных в CSV файл. Функция
# csv.DictWriter позволяет записывать данные в CSV файл, где каждый словарь из
# списка становится одной строкой в CSV.
# Подсказка № 3
# Обеспечьте правильное управление строками в CSV файле. При записи в CSV файл
# используйте параметр newline='' в open(), чтобы избежать дополнительных пустых
# строк между записями на Windows.

import json
import csv
import os

def read_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка декодирования JSON в файле {file_path}.")
        return []

def write_csv(data, file_path):
    """
    Записывает данные в CSV файл.

    :param data: Список словарей с данными о продуктах.
    :param file_path: Путь к выходному CSV файлу.
    """
    if not data:
        print("Нет данных для записи в CSV файл.")
        return

    fieldnames = data[0].keys()

    try:
        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print(f"Данные успешно записаны в {file_path}.")
    except Exception as e:
        print(f"Произошла ошибка при записи в CSV файл {file_path}: {e}")

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_file = os.path.join(script_dir, 'products.json')
    csv_file = os.path.join(script_dir, 'products.csv')
    products = read_json(json_file)
    write_csv(products, csv_file)

if __name__ == "__main__":
    main()