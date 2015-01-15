#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File Name: 165_compare_two_version.py
# Author: Haibin Huang
# Version: 1.0
# Create Date: 15-1-13


def compareVersion(version1, version2):
        v1 = version1.split('.', version1.count('.'))
        v2 = version2.split('.', version2.count('.'))
        lens1 = len(v1)
        lens2 = len(v2)
        if lens1 < lens2:
            for i in range(lens2-lens1):
                v1.append(0)
            length = lens2
        else:
            for i in range(lens1-lens2):
                v2.append(0)
            length = lens1
        for i in range(length):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1


if __name__ == '__main__':
    version1 = '01'
    version2 = '1'

    print compareVersion(version1, version2)

    a = []
    for i in range(0):
        print 'hhlo'
