## Reference
# http://www.lintcode.com/en/problem/rotate-list/#
# 61 https://leetcode.com/problems/rotate-list/#/description

## Tags - Medium; Blue
# Basic Implementation; Rotate; List

## Description
# Given a list, rotate the list to the right by k places, where k is non-negative.
# For example:
# Given 1->2->3->4->5->NULL and k==2, return 4->5->1->2->3->NULL

## Analysis
# 1) Brute-force: compared with array rotate, we have to traverse the linked list, and then find the rotate position
# in where, we can cut off, and re-connect them, therefore, we need dummy head, cut-head and a pre-head
# So the steps is dummy-head.next = cut_pos
# 2) Two-pointers: slow-fast pointers

## Solution
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution(object):
    # check list long first
    def getLen(self, head):
        if not head:
	    return 0
        counter = 0
        while head:
            head = head.next
            counter += 1
        return counter        

    def rotateRight(self, head, k):
        if not head or k == 0:
            return head
        N = self.getLen(head)
        k %= N
        if k == 0:
            return head
        slow, fast = head, head
        # walk fast k teps first
        for i in xrange(k):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        # now fast is the tail
        # and slow is the pre of rotate point
        newhead = slow.next
        slow.next = None
        tail.next = head
        #head = newhead
        return newhead

