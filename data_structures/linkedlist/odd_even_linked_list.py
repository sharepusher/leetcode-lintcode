## Reference
# https://www.lintcode.com/problem/odd-even-linked-list/description

## Medium - Microsoft

## Description
# Given a singly linked list, group all the nodes together followed by the even nodes.
# Please note here we are talking about the node number and not the value in the nodes.
# The relative order inside both the even and odd groups should remain as it was in the input.
# The first node is considered odd, the second node even and so on..

## Example
# Input: 1->2->3->4->5->NULL  Output: 1->3->5->2->4->NULL
# Input: 2->1->null   Output: 2->1->null

## Analysis
# 1. odd and even are the sequence of the linked list, but not the node value
# 2. while even_tail and even_tail.next, as odd.next = even.next, we need even.next to update odd
#    if even_tail.next is the None or even_tail is None, then they are the end.

## Solution
# 1. prepare one list, and traverse the linked list to store the nodes to list
#    and then traverse the list twice to link the odd and even separately
# 2. prepare two list, one for odd and one for even
# 3. tarverse once and re-connect the nodes properly

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    # param head: a singly linked list
    # return: Modified linked list

    def oddEvenList(self, head):
        if not head:
            return head
        odd_head = odd_tail = head
        even_head = even_tail = head.next

        while even_tail and even_tail.next:
            # update odd_tail
            odd_tail.next = even_tail.next
            odd_tail = odd_tail.next

            even_tail.next = odd.next
            even_tail = even_tail.next
            
        # connect odd and even list
        odd_tail.next = even_head
        return odd_head








