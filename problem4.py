#!/usr/bin/env python
# encoding: utf-8


def problem4():
    """
    A palindromic number reads the same both ways.
    The largest palindrome made from the product of two 2-digit numbers is
    9009 = 91 × 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    def isPalindromic(n):
        m = int(str(n)[::-1])
        if(m == n):
            return True
        else:
            return False

    Pali_list = []
    for i in range(91*99, 999*998, 1):
        if(isPalindromic(i)):
            for x in range(100, 999):
                if (i % x == 0):
                    y = i / x
                    if(len(str(y)) == 3):
                        Pali_list.append(i)
    return Pali_list[-1]


if __name__ == "__main__":
    print problem4()
