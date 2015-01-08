#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File Name: 171_excel_sheet_column_number.py
# Author: Haibin Huang
# Version: 1.0
# Create Date: 15-1-7


def titleToNumber(s):
    lens = len(s)
    num = 0
    i = 1
    for char in s:
        num += (ord(char.upper())-64) * 26**(lens-i)
        i += 1
    return num


if __name__ == '__main__':

    rs, rm = divmod(2, 26)
    s = ''
    s += chr(rm + 64)
    print s
    print titleToNumber('YZ')
