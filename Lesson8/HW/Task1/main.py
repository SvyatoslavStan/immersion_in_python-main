# Задание 1. Работа с основными данными
# Напишите функцию, которая получает на вход директорию и рекурсивно обходит
# её и все вложенные директории. Результаты обхода сохраните в файлы json, csv и
# pickle. Для дочерних объектов указывайте родительскую директорию. Для
# каждого объекта укажите файл это или директория. Для файлов сохраните его
# размер в байтах, а для директорий размер файлов в ней с учётом всех вложенных
# файлов и директорий. Соберите из созданных на уроке и в рамках домашнего
# задания функций пакет для работы с файлами разных форматов.
# Подсказка № 1
# Для рекурсивного обхода используйте функцию os.walk(). Эта функция генерирует
# имена файлов и директорий в указанной директории и ее поддиректориях. Внутри
# цикла можно разделять файлы и директории и собирать информацию о них.
# Подсказка № 2
# Используйте os.path.getsize() для определения размера файла. Эта функция
# возвращает размер файла в байтах. Для директорий вы можете использовать
# рекурсивный обход для вычисления общего размера всех вложенных файлов.
# Подсказка № 3
# Для сбора информации о каждом объекте создайте словарь. Словарь должен
# содержать такие ключи, как 'name', 'path', 'type', 'size', и 'parent'.
# Используйте os.path.basename() для получения имени родительской директории.
# Подсказка № 4
# Сохраняйте данные в разные форматы с помощью соответствующих библиотек.
# Используйте json.dump() для JSON, csv.DictWriter() для CSV и
# pickle.dump() для Pickle.


import os
import json
import csv
import pickle
from collections import defaultdict

def traverse_directory(directory):
    objects = []
    dir_sizes = defaultdict(int)

    for root, dirs, files in os.walk(directory, topdown=False):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                size = os.path.getsize(file_path)
            except OSError:
                size = 0
            parent = os.path.basename(root)
            obj = {
                'name': file,
                'path': file_path,
                'type': 'file',
                'size': size,
                'parent': parent
            }
            objects.append(obj)
            dir_path = root
            while True:
                dir_sizes[dir_path] += size
                parent_dir = os.path.dirname(dir_path)
                if parent_dir == dir_path:
                    break
                dir_path = parent_dir

        for dir in dirs:
            dir_path = os.path.join(root, dir)
            parent = os.path.basename(root)
            obj = {
                'name': dir,
                'path': dir_path,
                'type': 'directory',
                'size': dir_sizes.get(dir_path, 0),
                'parent': parent
            }
            objects.append(obj)

        obj = {
            'name': os.path.basename(root),
            'path': root,
            'type': 'directory',
            'size': dir_sizes.get(root, 0),
            'parent': os.path.basename(os.path.dirname(root)) if os.path.dirname(root) != root else None
        }
        objects.append(obj)

    return objects, dir_sizes

def save_to_json(data, filename):

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def save_to_csv(data, filename):

    if not data:
        return
    fieldnames = data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def save_to_pickle(data, filename):

    with open(filename, 'wb') as f:
        pickle.dump(data, f)

def main(directory, json_file, csv_file, pickle_file):
    objects, dir_sizes = traverse_directory(directory)
    save_to_json(objects, json_file)
    save_to_csv(objects, csv_file)
    save_to_pickle(objects, pickle_file)
    print(f"Данные успешно сохранены в {json_file}, {csv_file} и {pickle_file}")

if __name__ == "__main__":
    main(
        directory=r'C:\Users\Mrgton\Desktop\УЧЕБА',
        json_file='output.json',
        csv_file='output.csv',
        pickle_file='output.pkl'
    )

from pathlib import Path
import json
import csv
import pickle
from collections import defaultdict
import os

def traverse_directory(directory):
    """
    Рекурсивно обходит директорию и собирает информацию о файлах и поддиректориях.

    :param directory: Путь к начальной директории (Path объект).
    :return: Список словарей с информацией об объектах и словарь с размерами директорий.
    """
    objects = []
    dir_sizes = defaultdict(int)  

    for root, dirs, files in os.walk(directory, topdown=False):
        root_path = Path(root)
        # Обработка файлов
        for file in files:
            file_path = root_path / file
            try:
                size = file_path.stat().st_size
            except OSError:
                size = 0  
            parent = root_path.name
            obj = {
                'name': file,
                'path': str(file_path),
                'type': 'file',
                'size': size,
                'parent': parent
            }
            objects.append(obj)
            dir_path = root_path
            while True:
                dir_sizes[dir_path] += size
                if dir_path.parent == dir_path:
                    break
                dir_path = dir_path.parent

        for dir in dirs:
            dir_path = root_path / dir
            parent = root_path.name
            obj = {
                'name': dir,
                'path': str(dir_path),
                'type': 'directory',
                'size': dir_sizes.get(dir_path, 0),
                'parent': parent
            }
            objects.append(obj)

        obj = {
            'name': root_path.name,
            'path': str(root_path),
            'type': 'directory',
            'size': dir_sizes.get(root_path, 0),
            'parent': root_path.parent.name if root_path.parent != root_path else None
        }
        objects.append(obj)

    return objects, dir_sizes

def save_to_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def save_to_csv(data, filename):
    if not data:
        return
    fieldnames = data[0].keys()
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def save_to_pickle(data, filename):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

def main(directory, json_file, csv_file, pickle_file):
    objects, dir_sizes = traverse_directory(directory)
    save_to_json(objects, json_file)
    save_to_csv(objects, csv_file)
    save_to_pickle(objects, pickle_file)
    print(f"Данные успешно сохранены в {json_file}, {csv_file} и {pickle_file}")

if __name__ == "__main__":
    script_dir = Path(__file__).resolve().parent
    target_directory = Path(r'C:\Users\Mrgton\Desktop\УЧЕБА')
    json_output = script_dir / 'output.json'
    csv_output = script_dir / 'output.csv'
    pickle_output = script_dir / 'output.pkl'
    main(
        directory=target_directory,
        json_file=json_output,
        csv_file=csv_output,
        pickle_file=pickle_output
    )
