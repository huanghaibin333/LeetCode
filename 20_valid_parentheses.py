#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File Name: 20_valid_parentheses.py
# Author: Haibin Huang
# Version: 1.0
# Create Date: 15-1-13


def isValid(s):
    lens = len(s)
    if lens % 2:
        return False
    else:
        stack = ['e']
        for i in range(lens):
            if s[i] in '({[':
                stack.append(s[i])
            elif s[i] == ')' and stack[-1] == '(':
                stack.pop()
            elif s[i] == '}' and stack[-1] == '{':
                stack.pop()
            elif s[i] == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False
        if len(stack) != 1:
            return False
        else:
            return True


if __name__ == '__main__':
    s = '(('
    print isValid(s)