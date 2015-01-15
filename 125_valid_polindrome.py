#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File Name: 125_valid_polindrome.py
# Author: Haibin Huang
# Version: 1.0
# Create Date: 15-1-15

def isPalindrome(s):
    delset = [c.lower() for c in s if c.isalnum()]
    lens = len(delset)
    if lens != 0:
        for i in xrange(lens/2):
            if delset[i] != delset[lens-i-1]:
                return False
    return True


if __name__ == '__main__':
    line = 'A man, a plan, a canal: Panama'
    print isPalindrome(line)
    print isPalindrome('1a1')

    print '12a'.isalnum()

