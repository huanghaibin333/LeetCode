#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File Name: 70_climbing_stairs.py
# Author: Haibin Huang
# Version: 1.0
# Create Date: 15-1-15

import time


def A(n, m):
    result = 1.0
    if m -n < n:
        n = m-n
    while n:
        result *= m
        result /= n
        m -= 1
        n -= 1
    return int(result)

def stairs(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return stairs(n-1) + stairs(n-2)


def climbstairs(n):
    return climb_step(0, 1, n)


def climb_step(sum, count, max):
    if count > max:
        return sum
    return climb_step(sum+count, count+1, max)


def climbstairs(n):
    a = 1
    b = 1
    if n < 2:
        return 1
    else:
        while n-1:
            a, b = b, a+b
            n -= 1
        return b

if __name__ == '__main__':
    n = 100
    start = time.time()
    for n in range(1, 40):
        result = 0
        size = n // 2 + 1
        for i in range(size):
            k = A(i, n-i)
            #print k
            result += k
    print result
    end = time.time()
    print 'time=', end-start

    start = time.time()
    print stairs(n)
    end = time.time()
    print 'time=', end-start


    start = time.time()
    print climbstairs(n)
    end = time.time()
    print 'time=', end-start

#    print stairs(35)
