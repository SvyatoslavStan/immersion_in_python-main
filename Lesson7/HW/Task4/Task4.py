# Задача 4. Поиск файлов по расширению
# Напишите функцию, которая находит и перечисляет все файлы с заданным
# расширением в указанном каталоге и всех его подкаталогах. Функция должна
# принимать путь к каталогу и расширение файла.
# Подсказка № 1
# Используйте os.walk() для рекурсивного обхода указанного каталога. Это позволяет
# вам обрабатывать все файлы в текущем каталоге и во всех его подкаталогах.
# Подсказка № 2
# Используйте метод str.endswith() для проверки, имеет ли имя файла указанное
# расширение. Это поможет вам отфильтровать файлы по заданному типу.
# Подсказка № 3
# Используйте os.path.join() для объединения пути к каталогу и имени файла,
# чтобы получить полный путь к файлу. Это поможет корректно обрабатывать файлы в
# разных каталогах.

import os

def find_files_by_extension(directory, extension):

    if not os.path.isdir(directory):
        print(f"Каталог '{directory}' не найден.")
        return
    found_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                full_path = os.path.join(root, file)
                found_files.append(full_path)

    if found_files:
        print(f"Найдено {len(found_files)} файл(ов) с расширением '{extension}':")
        for file_path in found_files:
            print(file_path)
    else:
        print(f"Файлы с расширением '{extension}' не найдены в каталоге '{directory}'.")

find_files_by_extension(
    directory="путь/к/каталогу",  
    extension=".txt"              
)
