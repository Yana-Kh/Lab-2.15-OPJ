#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

"""
Создает новую дериктоию и прописывает путь к ней
в текстовом файле с последующем переименованием 
этого файла
"""

if __name__ == '__main__':
    # Создание директории и запоминание пути
    dir_name = input("Введите имя директории: ")
    os.mkdir(dir_name)
    path = os.getcwd()

    #Перемещение в новую директорию
    os.chdir(r"{0}\{1}".format(path, dir_name))
    with open("file.txt", "w", encoding="utf-8") as f:
        # appending the content to the file
        f.write(os.getcwd())

    #Переименование файла
    new_name = input("Введите новое имя для файла: ")
    os.rename("file.txt", new_name)
