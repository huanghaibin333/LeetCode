#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File Name: 66_plus_one.py
# Author: Haibin Huang
# Create Date: 2015/1/16

def plusOne(digits):
    Flag = 1
    for i in range(len(digits)-1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
            if i == 0:
                digits.insert(0, 1)
                break
        else:
            digits[i] += Flag
            break
    return digits


if __name__ == '__main__':
    list = [9, 9, 9]
    print plusOne(list)
