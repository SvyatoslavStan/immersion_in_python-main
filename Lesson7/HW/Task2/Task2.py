# Задача 2. Создание архива каталога
# Напишите скрипт, который создает архив каталога в формате .zip. Скрипт
# должен принимать путь к исходному каталогу и путь к целевому архиву. Архив
# должен включать все файлы и подпапки исходного каталога.
# Подсказка № 1
# Используйте функцию os.walk() для обхода всех файлов и подпапок в исходном
# каталоге. Это функция возвращает корневую папку, список директорий и список
# файлов в каждом корневом каталоге.
# Подсказка № 2
# Для создания архива используйте zipfile.ZipFile() с режимом 'w' для записи.
# Также передайте параметр zipfile.ZIP_DEFLATED, чтобы применить сжатие к
# файлам в архиве.
# Подсказка № 3
# Чтобы сохранить структуру каталогов в архиве, используйте функцию
# os.path.relpath(), чтобы добавить файлы в архив с путями относительно
# исходного каталога.
# Подсказка № 4
# Для получения полного пути к файлу используйте os.path.join(root, file), где
# root - это текущая корневая папка, а file - это имя файла.
# Подсказка № 5
# Перед созданием архива убедитесь, что исходный каталог существует, чтобы избежать
# ошибок. Используйте os.path.isdir() для проверки существования каталога.

import os
import zipfile

def create_zip_archive(source_directory, target_archive):

    if not os.path.isdir(source_directory):
        print(f"Каталог '{source_directory}' не найден.")
        return


    with zipfile.ZipFile(target_archive, 'w', zipfile.ZIP_DEFLATED) as zipf:

        for root, dirs, files in os.walk(source_directory):
            for file in files:
                full_path = os.path.join(root, file)
                relative_path = os.path.relpath(full_path, source_directory)

                zipf.write(full_path, relative_path)

    print(f"Архив '{target_archive}' успешно создан.")

create_zip_archive(
    source_directory="путь/к/исходному/каталогу",  
    target_archive="путь/к/целевому/архиву.zip"    
)
