#!/usr/bin/env python
# encoding: utf-8
from timeout import timethis


def isprime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in xrange(3, int(n ** 0.5) + 1, 2):  # skip 1 number at a time
        if n % i == 0:
            return False
    return True


def nextprime(n):
    while True:
        n += 1
        if isprime(n):
            return n


@timethis
def problem10():
    """
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million.
    """
    limit = 2000000

    curr = 2
    result = 0
    while(curr < limit):
        result += curr
        curr = nextprime(curr)
    return result


if __name__ == "__main__":
    print problem10()
