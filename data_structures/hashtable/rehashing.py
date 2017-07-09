## Reference
# http://www.lintcode.com/en/problem/rehashing/

## Tags - Medium
# Hash Table; Lintcode Copyright

## Description
# The size of the hash table is not determinate at the very beginning.
# If the total size of keys is too large(e.g. size>=capacity/10), we should double 
# the size of the hash table and rehash every keys. Say you have a hash table looks like:
# [null, 21, 14, null]
#        ↓    ↓
#        9   null
#        ↓
#       null
# The hash function is:
# int hashcode(int key, int capacity) {
#     return key % capacity; 
# }
# here we have three numbers, 9, 14, and 21, where 21 and 9 share the same position as they all
# have the same hashcode 1 (21 % 4 = 9 % 4 = 1). We store them in the hash table by linked list.
# Rehashing this hash table, double the capacity. you will git 
# size=3, capacity=8
# index:   0    1    2    3     4    5    6   7
# hash : [null, 9, null, null, null, 21, 14, null]
# Given the original hash table, return the new hash table after rehashing.
# NOTICE:
# For negative integer in hash table, the position can be calculated as below
# C++/Java: if you directly calculate -4 % 3 you will get -1. 
   You can use function: a % b = (a % b + b) % b to make it is a non negative integer.
# Python: you can directly use -1 % 3, you will get 2 automatically
# Example:
# Given [null, 21->9->null, 14->null, null]
# return [null, 9->null, null, null, null, 21->null, 14->null, null]

## Solution
# Definition of listNode
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    # double the size of hashTable
    def rehashing(self, hashTable):
        # prepare and init 
        current = len(hashTable)
        new_capacity = 2*current
        # the init should be None, when there's value, it should be a linked list with value.
        new_hash = [None]*new_capacity
        # rehashing and merge the old to new one
        for node in hashTable:
            while node:
                hash_code = node.val % new_capacity
                if not new_hash[hash_code]:
                    new_hash[hash_code] = ListNode(node.val)
                else:
                    # now new hash hash linked list already
                    # walk to find the tail
                    tail = new_hash[hash_code]
                    while tail.next:
                        tail = tail.next
                    tail.next = ListNode(node.val)
                node = node.next
        return new_hash 
                
