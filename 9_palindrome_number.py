#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File Name: 9_palindrome_number.py
# Author: Haibin Huang
# Version: 1.0
# Create Date: 15-1-15


def bits_of_number(num):
    n = 0
    while num:
        n += 1
        num /= 10
    return n


def isPalindrome(x):
    if x < 0:
        return False
    else:
        bits = 0
        num = x
        while num:
            bits += 1
            num /= 10
        count = bits / 2
        for i in range(count):
            last = x % 10
            first= x // (10**(bits - i*2 - 1))
            if first != last:
                return False
            x = x / 10 % (10**(bits - i*2 -2))
        return True

if __name__ == '__main__':

    print bits_of_number(1234)
    print isPalindrome(10)
    print isPalindrome(121)
    print isPalindrome(123321)
    print isPalindrome(1236321)
    print isPalindrome(1232321)


    print 10 ** 2