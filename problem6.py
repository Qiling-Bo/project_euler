#!/usr/bin/env python
# encoding: utf-8


def problem6():
    """
    The sum of the squares of the first ten natural numbers is,
    1**2 + 2**2 + ... + 10**2 = 385
    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)**2 = 55**2 = 3025
    Hence the difference between the sum of the squares of the first ten
    natural numbers and the square of the sum is 3025 − 385 = 2640.
    Find the difference between the sum of the squares of the first one
    hundred natural numbers and the square of the sum.
    """
    square_sum, sum_square = 0, 0
    for i in range(1, 101):
        square_sum += i**2
        sum_square += i
    sum_square = sum_square**2
    result = sum_square - square_sum
    return result


if __name__ == "__main__":
    print problem6()
