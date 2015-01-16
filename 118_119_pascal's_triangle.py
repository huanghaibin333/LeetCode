#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File Name: 118_pascal's_triangle.py
# Author: Haibin Huang
# Version: 1.0
# Create Date: 15-1-16


def generate(numRows):
    triangle = []
    for num in range(numRows):
        if num == 0:
            triangle.append([1])
        elif num == 1:
            triangle.append([1, 1])
        else:
            lastRow = [1]
            for i in range(1, num):
                lastRow.append(triangle[num-1][i] + triangle[num-1][i-1])
            lastRow.append(1)
            triangle.append(lastRow)
    return triangle


def getRow(rowIndex):
    for num in range(rowIndex+1):
        if num == 0:
            triangle = [1]
        elif num == 1:
            triangle = [1, 1]
        else:
            lastRow = [1]
            for i in range(1, num):
                lastRow.append(triangle[i] + triangle[i-1])
            lastRow.append(1)
            triangle = lastRow
    return triangle



if __name__ == '__main__':
    for i in range(4):
        print getRow(i)