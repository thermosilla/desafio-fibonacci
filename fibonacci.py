# -*- coding: utf-8 -*-
from math import sqrt, pow, log, fabs


def fib(n):
    """Calcula el número n de la secuencia fibonacci, usando la formula de Binet"""
    return int((pow(1 + sqrt(5), n) - pow(1 - sqrt(5), n)) / (pow(2, n) * sqrt(5)))


def fib_inv(f):
    """Calcula posición de número fibonacci más cercano menor a f, por medotodo de aproximación numérica"""
    pos_fib = int(
        round((log(f) + log(sqrt(5))) / (log(1 + sqrt(5)) - log(2))))

    if fib(pos_fib) <= f:
        return pos_fib
    else:
        return pos_fib - 1


def cuenta_fib(a, b):
    """Retorna la cantidad de números fibonacci entre a y b"""
    count_fib = int(fabs(fib_inv(b) - fib_inv(a)))
    if count_fib == 0:
        if (fib(fib_inv(a)) == a) or ((fib(fib_inv(b)) == b)):
            return 1
    return count_fib
