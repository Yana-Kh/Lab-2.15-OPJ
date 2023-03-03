#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    file_name = input("Введите имя редактируемого файла: ")
    words_name = input("Введите имя файла со словами: ")
    words = []

    # Чтение файла со служебными словами
    with open(words_name, "r", encoding="utf-8") as f:
        words = f.readlines()

    # Открытие файла для записи
    with open("new2.txt", "w", encoding="utf-8") as new_f:

        # Чтение заданного файла
        with open(file_name, "r+", encoding="utf-8") as f:
            sentences = f.readlines()
            for sentence in sentences:
                for i in words:
                    if i[:-1] in sentence:
                        sentence = sentence.replace(i[:-1], "*" * (len(i) - 1))
                # Запись в файл нововй версии
                new_f.write(sentence)

    print("Операция прошла успешно")
