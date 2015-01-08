#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File Name: excel_sheet_column_title.py
# Author: Haibin Huang
# Version: 1.0
# Create Date: 15-1-8
def convertToTitle(num):
    s = ''
    result, reminder = divmod(num, 26)
    if reminder:
        s += chr(reminder+64)
    else:
        s += 'Z'
        result -= 1

    while result:
        result, reminder = divmod(result, 26)
        if reminder:
            s = chr(reminder+64) + s
        else:
            s = 'Z' + s
            result -= 1
    return s


if __name__ == '__main__':

    rs, rm = divmod(2, 26)
    s = ''
    s += chr(rm + 64)
    print s
    print convertToTitle(676)