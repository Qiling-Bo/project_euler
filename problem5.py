#!/usr/bin/env python
# encoding: utf-8


def problem5():
    """
    2520 is the smallest number that can be divided by each of the numbers
    from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of
    the numbers from 1 to 20?
    """
    limit = 20

    def gcd(a, b):
        #最大公约数
        while(b > 0):
            a, b = b, a % b
        return a

    def lcm(a, b):
        #最小公倍数
        return (a * b) / gcd(a, b)

    # 依次求1和2，直到20的最小公倍数
    return reduce(lcm, range(1, limit + 1), 1)


if __name__ == "__main__":
    print problem5()
