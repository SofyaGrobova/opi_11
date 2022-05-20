#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from threading import Thread
import math


eps = .0000001


def sum(x):
    n = 1
    s = 1
    curr = 1
    previous = 0
    while True:
        if abs(s - previous) < eps:
            break
        curr = curr * (n + 1) * x
        previous = s
        s += curr
        print(s)
        n += 1
        if n > 6:
            break

    print(f"Сумма ряда для значения {x}: {s}")
    print(f"Проверка: 1/(1 - {x})^2 = {1 / math.pow((1 - x), 2)}")


if __name__ == '__main__':
    thread1 = Thread(target=sum, args=(-0.7,))
    thread2 = Thread(target=sum, args=(3,))
    thread1.start()
    thread2.start()
