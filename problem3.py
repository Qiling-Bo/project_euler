#!/usr/bin/env python
# encoding: utf-8


def problem3():
    """
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
    """
    x = 600851475143

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

    def maxfactor(n):
        if isprime(n):
            return n
        else:
            i = 2
            while(i < n):
                if (n % i == 0):
                    print "factor: " + str(i)
                    n = n / i
                    print "num: " + str(n)
                    result = maxfactor(n)
                    return result
                i = nextprime(i)

    return maxfactor(x)


if __name__ == "__main__":
    print problem3()
