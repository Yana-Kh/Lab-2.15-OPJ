# -*- coding: utf-8 -*-
import re

if __name__ == '__main__':
    with open("text1.txt", "r", encoding="utf-8") as f:
        sentences = f.readlines()

        print("Предложения с 2-значными числами:")
        # Вывод предложений с двухзначными числами.
        for sentence in sentences:
            result = re.findall(r'(\d{2,})', sentence)
            if result:
                print(sentence)
