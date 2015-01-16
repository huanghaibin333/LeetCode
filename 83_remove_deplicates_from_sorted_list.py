#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File Name: 83_remove_deplicates_from_sorted_list.py
# Author: Haibin Huang
# Version: 1.0
# Create Date: 15-1-16


class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None


def deleteDuplicates(head):
    if isinstance(head, ListNode):
        node = head
        while node.next:
            if node.val != node.next.val:
                node = node.next
            else:
                node.next = node.next.next
        return head



if __name__ == '__main__':
    node = []
    node.append(ListNode(0))
    for i in range(1, 10, 1):
        node.append(ListNode(i))
        node[i-1].next = node[i]

    node[6].val = 5
    node0 = node[0]

    afterdelete = deleteDuplicates(node0)
    for i in range(8):
        print afterdelete.val
        afterdelete = afterdelete.next