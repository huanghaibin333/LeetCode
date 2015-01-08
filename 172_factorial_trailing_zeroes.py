#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File Name: 172_factorial_trailing_zeroes.py
# Author: Haibin Huang
# Version: 1.0
# Create Date: 15-1-8


def trailingZeroes(n):
    zeros = 0
    flag = n//5
    while flag:
        zeros += flag
        flag //= 5
    return zeros


def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        return factorial(n-1L)*n


def zero(n):
    i = 0
    results, mod = divmod(n, 10)
    while not mod:
        results, mod = divmod(results, 10)
        i += 1
    return i


if __name__ == '__main__':
    for n in range(100, 300, 5):
        result = factorial(n)
        print n, trailingZeroes(n), zero(result), result

