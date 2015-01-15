#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File Name: 26_remove_duplicates.py
# Author: Haibin Huang
# Version: 1.0
# Create Date: 15-1-15


def removeDuplicates(A):
    i = 0
    a = list(set(A))
    a.sort()
    for char in a:
        A[i] = char
        i += 1
    return len(a)

if __name__ == '__main__':
    A = [-1, 1, 2, 4, 5, 6, 6, 7, 7, 8, 9]
    print set(A)
    print removeDuplicates(A)
    print A