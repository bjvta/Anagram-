"""Fibo Module"""


def fibo(n):
    if n <= 1:
        return 1
    return fibo(n - 1) + fibo(n - 2)


def fibo_v2():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
      
