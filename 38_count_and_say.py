#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File Name: 38_count_and_say.py
# Author: Haibin Huang
# Create Date: 2015/1/20


def countAndSay(n):
    for index in xrange(1, n+1):
        if index == 1:
            last = '1'
        elif index == 2:
            last = '11'
        else:
            start = 0
            temp = ''
            count = 1
            for i in range(1, len(last)):
                if last[i] == last[i-1]:
                    count += 1
                else:
                    temp += (str(count)+str(last[i-1]))
                    count = 1
            last = temp + str(count) + str(last[i])

    return last


if __name__ == '__main__':
    for i in range(1, 11):
        print countAndSay(i)