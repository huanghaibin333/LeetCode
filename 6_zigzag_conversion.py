#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File Name: 6_zigzag_conversion.py
# Author: Haibin Huang
# Version: 1.0
# Create Date: 15-1-8

import time


def convert(s, nRows):
    if nRows == 1:
        return s
    else:
        rows = []
        for i in range(nRows):
            rows.append([])
        index = 1
        j = 1
        flag = 1
        lens = len(s)
        if lens:
            rows[0].append(s[0])
        else:
            return ''
        while j < lens:
            rows[index].append(s[j])
            if not index % (nRows-1):
                flag = -flag
            index += flag
            j += 1
        str = ''
        for list in rows:
            str += ''.join(list)
        return str


if __name__ == '__main__':
    s = 'dspxdczzwgdgxqmqmgjwmqkxqdjqvbuatkzwoyxkeascrgufmgezwoyotjgokbqflpdznalsbgwumsbzyhyxvylqhseut'
    start = time.time()
    print convert(s, 75)
    end = time.time()
    print 'time:', end-start