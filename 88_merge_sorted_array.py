#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File Name: 88_merge_sorted_array.py
# Author: Haibin Huang
# Version: 1.0
# Create Date: 15-1-13


def merge1(A, m, B, n):
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



def merge(A, m, B, n):
    if m == 0 and n == 0:
        pass
    elif m < n:
        A, m, B, n

    i = 0
    for b in B:
        j = m - 1
        if b <= A[i]:
            A.insert(i, b)
        elif b > A[j]:
            A.append(b)
        else:
            while (j - i) >1:
                # print i, j
                k = (i+j)/2
                if b <= A[k]:
                    j = k
                else:
                    i = k
            i = (i+j)/2 + 1
            j += 1
            A.insert(i, b)


if __name__ == '__main__':
    A = []
    C = [0, 2, 4, 6, 9, 10, 11, 12, 26, 35, 43, 56, 100, 120]
    B = [1]
    print A
    print B
    merge1(A, len(A), B, len(B))
    print A
