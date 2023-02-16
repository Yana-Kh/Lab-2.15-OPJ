#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    with open("text1.txt", "r", encoding="utf-8") as f:
        sentences = f.readlines()

        print("Предложения с 2-значными числами:")
        # Вывод предложений с двухзначными числами.
        for sentence in sentences:
            for ind, i in enumerate(sentence):
                if (i.isdigit() and ind != len(sentence) and
                        sentence[ind + 1].isdigit()):
                    print(sentence)
