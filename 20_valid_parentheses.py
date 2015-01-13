#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File Name: 20_valid_parentheses.py
# Author: Haibin Huang
# Version: 1.0
# Create Date: 15-1-13


def isValid(s):
    lens = len(s)
    if not lens:
        return True
    else:
        if s[0] in ')}]':
            return False
        else:
            stack = []
            stack.append(s[0])
            for i in range(1, lens):
                if s[i] in '({[':
                    stack.append(s[i])
                elif s[i] == ')':
                    if len(stack) and stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                elif s[i] == '}':
                    if len(stack) and stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                elif s[i] == ']':
                    if len(stack) and stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
        if len(stack):
            return False
        else:
            return True


if __name__ == '__main__':
    s = '(])'
    print isValid(s)