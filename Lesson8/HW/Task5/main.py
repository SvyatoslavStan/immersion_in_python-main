# Задача 5. Конвертация CSV в JSON с изменением структуры данных
# Напишите скрипт, который считывает данные из CSV файла и сохраняет их в
# JSON файл с другой структурой. CSV файл содержит данные о книгах (название,
# автор, год издания). В JSON файле данные должны быть сгруппированы по
# авторам, а книги каждого автора должны быть записаны как список.
# Пример: Из файла books.csv нужно создать файл books_by_author.json, где
# книги сгруппированы по авторам.
# Подсказка № 1
# Используйте csv.DictReader для чтения данных из CSV файла. Эта функция читает
# данные из CSV файла и преобразует каждую строку в словарь, где ключи
# соответствуют заголовкам столбцов.
# Подсказка № 2
# Создайте словарь, где ключи будут авторами, а значения — списками книг.
# Используйте словарь для группировки книг по авторам. Для каждого автора создавайте
# список книг, который будет заполняться по мере чтения CSV файла.
# Подсказка № 3
# Преобразуйте данные в формат JSON с помощью json.dump(). После того как данные
# сгруппированы, используйте json.dump() для записи данных в файл JSON.
# Убедитесь, что данные имеют нужный формат и структуру.

import csv
import json
import os

def read_books_csv(file_path):
    books = []
    try:
        with open(file_path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                books.append(row)
        return books
    except FileNotFoundError:
        print(f"Файл {file_path} не найден.")
        return []
    except Exception as e:
        print(f"Произошла ошибка при чтении файла {file_path}: {e}")
        return []

def group_books_by_author(books):
    books_by_author = {}
    for book in books:
        author = book.get('author')
        title = book.get('title')
        year = book.get('year')

        if author is None or title is None or year is None:
            print(f"Некорректная запись: {book}. Пропуск.")
            continue

        if author not in books_by_author:
            books_by_author[author] = []
        books_by_author[author].append({
            'title': title,
            'year': year
        })

    return books_by_author

def write_books_json(books_by_author, output_file):
    try:
        with open(output_file, 'w', encoding='utf-8') as jsonfile:
            json.dump(books_by_author, jsonfile, ensure_ascii=False, indent=4)
        print(f"Данные успешно записаны в {output_file}.")
    except Exception as e:
        print(f"Произошла ошибка при записи в файл {output_file}: {e}")

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    books_csv = os.path.join(script_dir, 'books.csv')
    books_json = os.path.join(script_dir, 'books_by_author.json')
    books = read_books_csv(books_csv)

    if not books:
        print("Нет данных для обработки. Завершение программы.")
        return
    books_by_author = group_books_by_author(books)

    if not books_by_author:
        print("Нет агрегированных данных для записи. Завершение программы.")
        return
    write_books_json(books_by_author, books_json)

if __name__ == "__main__":
    main()
