#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File Name: 88_merge_sorted_array.py
# Author: Haibin Huang
# Version: 1.0
# Create Date: 15-1-13


def merge(A, m, B, n):
    if m == 0:
        for b in B:
            A.append(b)
    else:
        i = 0
        j = m - 1
        for b in B:
            l = j
            if b <= A[i]:
                A.insert(i, b)
            elif b > A[l]:
                A.append(b)
            else:
                while (l - i) >1:
                    # print i, j
                    k = (i+l)/2
                    if b <= A[k]:
                        l = k
                    else:
                        i = k
                i = (i+l)/2 + 1
                A.insert(i, b)
            j += 1


if __name__ == '__main__':
    A = []
    B = [0, 2, 4, 6, 9, 10, 11, 12, 26, 35, 43, 56, 100, 120]
    print A
    print B
    merge(A, len(A), B, len(B))
    print A
    del A[::]
    print A
