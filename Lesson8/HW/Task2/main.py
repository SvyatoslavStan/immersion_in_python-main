# Задача 2. Объединение данных из нескольких JSON файлов
# Напишите скрипт, который объединяет данные из нескольких JSON файлов в
# один. Каждый файл содержит список словарей, описывающих сотрудников
# компании (имя, фамилия, возраст, должность). Итоговый JSON файл должен
# содержать объединённые списки сотрудников из всех файлов.
# Пример: У вас есть три файла employees1.json, employees2.json,
# employees3.json. Нужно объединить их в один файл all_employees.json.
# Подсказка № 1
# Используйте функцию glob.glob() для поиска всех JSON файлов в указанной
# директории.
# Подсказка № 2
# Откройте каждый JSON файл с помощью json.load() и добавьте данные в общий
# список. Функция json.load() позволяет прочитать содержимое JSON файла и
# преобразовать его в Python объект. Используйте list.extend() для объединения
# данных.
# Подсказка № 3
# Сохраните объединенные данные в новый JSON файл с помощью json.dump(). После
# объединения данных, используйте json.dump() для записи списка в новый JSON
# файл.

import glob
import json
import os

def find_json_files(directory, pattern="employees*.json"):
    search_pattern = os.path.join(directory, pattern)
    json_files = glob.glob(search_pattern)
    return json_files

def merge_employee_data(json_files):
    all_employees = []
    for file in json_files:
        try:
            with open(file, 'r', encoding='utf-8') as f:
                employees = json.load(f)
                if isinstance(employees, list):
                    all_employees.extend(employees)
                else:
                    print(f"В файле {file} содержатся некорректные данные (ожидается список).")
        except json.JSONDecodeError:
            print(f"Ошибка декодирования JSON в файле {file}.")
        except Exception as e:
            print(f"Произошла ошибка при обработке файла {file}: {e}")
    return all_employees

def save_to_json(data, output_file):
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Объединенные данные успешно сохранены в {output_file}.")
    except Exception as e:
        print(f"Произошла ошибка при сохранении данных в файл {output_file}: {e}")

def main(directory, output_file="all_employees.json"):
    json_files = find_json_files(directory)
    if not json_files:
        print(f"В директории {directory} не найдено файлов, соответствующих шаблону 'employees*.json'.")
        return

    print(f"Найдено {len(json_files)} JSON файлов для объединения.")
    all_employees = merge_employee_data(json_files)
    print(f"Объединено {len(all_employees)} сотрудников.")

    save_to_json(all_employees, output_file)


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    target_directory = script_dir
    output_json = os.path.join(script_dir, 'all_employees.json')
    main(directory=target_directory, output_file=output_json)
