#!/usr/bin/env python
# encoding: utf-8


def problem7():
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
    we can see that the 6th prime is 13.
    What is the 10 001st prime number?
    """
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
    i = 1
    p = 2
    while(i < 10001):
        p = nextprime(p)
        i += 1
        print str(i) + " : " + str(p)
    return p


if __name__ == "__main__":
    print "result: " + str(problem7())
