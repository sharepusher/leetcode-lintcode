## Reference
# http://www.lintcode.com/en/problem/reverse-linked-list/#
# 206 https://leetcode.com/problems/reverse-linked-list/#/description

## Tags - Easy; RED
# Linked list; Uber; Facebook

## Description
# Reverse a linked list.
# Example:
# For linked list 1->2->3, the reversed linked list is 3->2->1

## Challenge
# Reverse in-place and in one-pass.

## Analysis
# 1) stack + traverse: O(N)time; O(N)space; two pass
# 2) 3step reverse in-place, and in one pass

## Solutions
# definition of listNode
class ListNode(object):
    def __init__(self, val, next=None):
	self.val = val
	self.next = next
class Solution(object):
    # stack + traverse
    def reverse(self, head):
	if not head:
	    return head
	stack = []
	while head:
	    stack.append(head)
	    head = head.next
	# pop 
	head = stack.pop()
	tail = head
	while stack:
	   tail.next = stack.pop()
	   tail = tail.next
	tail.next = None
	return head

    # reverse in place and in one pass
    def reverse(self, head):
	if not head:
	    return head
	newhead = None
	while head:
	    tmp = head.next
	    head.next = newhead
	    newhead = head
	    head = tmp
	     
        return newhead

