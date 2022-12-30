"""Test Fibo module"""

from lib.fibo import fibo, fibo_v2


def test_fib_5_get_8():
    given = 5
    expected = 8
    assert fibo(given) == expected


def test_fib_8_get_34():
    given = 8
    expected = 34
    assert fibo(given) == expected


def test_fib_3_get_5():
    given = 4
    expected = 5
    assert fibo(given) == expected
    


def test_fibo_v2():
    fib_v2 = fibo_v2()
    assert next(fib_v2) == 0
    assert next(fib_v2) == 1
    assert next(fib_v2) == 1
    assert next(fib_v2) == 2
    assert next(fib_v2) == 3
    assert next(fib_v2) == 5