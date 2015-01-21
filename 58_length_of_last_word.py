#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File Name: 58_length_of_last_word.py
# Author: Haibin Huang
# Create Date: 2015/1/18
import time


def executeTime(fn):
    def wrappper(*args, **kwargs):
        start = time.time()
        ret = fn(*args, **kwargs)
        end = time.time()
        print 'Execute Time:', end-start
        return ret
    return wrappper


@executeTime
def lengthOfLastWord(s):
    word = s.split(' ', s.count(' '))
    for i in range(len(word)-1, -1, -1):
        if len(word[i]):
            return len(word[i])
    return 0

if __name__ == '__main__':
    s = "Hello world  "
    print lengthOfLastWord(s)