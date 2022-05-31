def fibonacci(n):
    """
    The fibonacci function takes in a one argument
    (n) and return the nth value off fibonacci series
    0, 1, 2, 3, 5, 8, 13, ..
    fibonacci formula is:

    fibonacci(n-1) + fibonacci(n-2)
    where n of 0 = 0 and n oof 1 = 1
    :param n:
    :return:
    """

    if n == 1 or n == 0:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    """
    The lucas function takes one argument (n) and
    return the nth Fibonacci number

    lucas series:
    2, 1, 3, 4, 7, 11, 18, 29, ...

    lucas equation:
    lucas(n) = lucas(n-1) + lucas(n-2)
    :param n:
    :return:
    """

    if n==0:
        return 2
    elif n==1:
        return 1
    else:
        return lucas(n-1) + (n-2)

def sum_series(n, first=0, second=1):
    """
    The sum_series function takes one required
    argument (n) and two optional arguments
    (first) and (second) which takes the first
    and the second arguments of a template of Fibonacci series

    option1, option2, (n-1)+(n-2) + ........

     Lucas series:
    first, second, first+second, first+2second, 2first+3second,  3first+5second, ...
    Lucas equation:
    lucas(n) = lucas(n-1) + lucas(n-2)
    :return:
    """

    if n==0:
        return first
    elif n==1:
        return second
    else:
        return sum_series(n-1, first, second) + sum_series(n-2, first, second)