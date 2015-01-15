#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File Name: 169_majority_element.py
# Author: Haibin Huang
# Version: 1.0
# Create Date: 15-1-13

import time
def majorityElement(num):
    lens = len(num)
    max = 0
    for i in set(num):
        count = num.count(i)
        if count > lens/2:
            major = i
            break
        elif count > max:
            major = i
            max = count
    return major


def majorityElement2(num):
    lens = len(num)
    max = 0
    myset = []
    for i in num:
        if i in myset:
            pass
        else:
            myset.append(i)
            count = num.count(i)
            if count > lens/2:
                major = i
                break
            elif count > max:
                major = i
                max = count
    return major


if __name__ == '__main__':
    num = [1, 2, 3, 45, 5, 4, 4, 6, 6, 4, 2, 3, 4, 5, 6, 6, 6]
    print set(num)
    lens = len(num)
    max = 0
    for i in set(num):
        count = num.count(i)
        if count > lens/2:
            major = i
            break
        elif count > max:
            major = i
            max = count
    print major
    start = time.time()
    majorityElement(num)
    middle = time.time()
    majorityElement2(num)
    end = time.time()
    print 'majorityElement', middle-start
    print 'majorityElement2', end-middle
