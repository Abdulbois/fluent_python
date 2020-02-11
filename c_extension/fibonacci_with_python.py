from time import time

import fibonacci


def time_dec(func):
    def wrapper(*args, **kwargs):
        t0 = time()
        result = func(*args, **kwargs)
        print(time() - t0)
        return result
    return wrapper


@time_dec
def fibonacci_py(n):
    return calc_fibonacci_py(n)


def calc_fibonacci_py(n):
    a = 0
    b = 1
    if n == 0:
        return a
    for i in range(2, n):
        c = a + b
        a = b
        b = c
    return b


@time_dec
def fibonacci_c(n):
    return fibonacci.fibonacci(n)


def main():
    print(fibonacci_py(22))
    print(fibonacci_c(22))


if __name__ == '__main__':
    main()
