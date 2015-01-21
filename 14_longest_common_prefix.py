#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File Name: 58_length_of_last_word.py
# Author: Haibin Huang
# Create Date: 2015/1/18

import time
import functools

def executeTime(fn):
    @functools.wraps(fn)
    def wrappper(*args, **kwargs):
        start = time.time()
        ret = fn(*args, **kwargs)
        end = time.time()
        print 'Execute Time: %s' % str(end - start)
        return ret

    return wrappper


#@executeTime
def longestcommonprefix(strs):
    if not len(strs):
        return ''
    minlen = len(strs[0])
    for i in strs:
        lens = len(i)
        if lens < minlen:
            minlen = lens
    if not lens:
        return ''
    else:
        prefix = ''
        for i in range(1,minlen+1):
            prefix = strs[0][:i]
            for j in strs:
                if prefix != j[:i]:
                    if len(prefix) == 1:
                        return ''
                    else:
                        return prefix[:i-1]
        return prefix


if __name__ == '__main__':
    str =["flower","flow","flight"]
    print longestcommonprefix(str)