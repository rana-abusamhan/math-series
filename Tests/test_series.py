import pytest
from math_series.series import fibonacci, lucas, sum_series

def test_fibonacci_0():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected

def test_fibonacci_1():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected

def test_fibonacci_5():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected

def test_fibonacci_7():
    assert 13 == fibonacci(7)

def test_lucas_0():
    actual = lucas(0)
    expected = 2
    assert actual == expected

def test_lucas_1():
    actual = lucas(1)
    expected = 1
    assert actual == expected

#     2, 1, 3, 4, 7, 11
def test_sum_series_as_lucas_5():
    actual = sum_series(5,2,1)
    expected = 11
    assert actual == expected

#     2, 3, 5, 8, 13, 21, 34, 55
def test_sum_series_as_lucas_7():
    actual = sum_series(7,2,3)
    expected = 55
    assert actual == expected

# optinal 0, 1, 1, 2, 3,
def test_sum_series_as_lucas_4():
    actual = sum_series(4)
    expected = 3
    assert actual == expected