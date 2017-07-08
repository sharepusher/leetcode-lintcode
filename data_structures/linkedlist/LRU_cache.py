## Reference
# http://www.lintcode.com/en/problem/lru-cache/#
# 146 https://leetcode.com/problems/lru-cache/#/description

## Tags - Linked List; RED
# Linked List; Google; Uber; Zenefits

## Description
# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations:
# get and put.
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should 
# invalidate the least recently used item before inserting a new item.
# Follow up: 
# Could you do both operation in O(1) time complexity.
# Example:
# LRUCache cache = new LRUCache(2) /*Capacity*/;
# cache.put(1, 1);  cache.put(2, 2);
# cache.get(1); //return 1
# cache.put(3, 3); // evicts key 2
# cache.get(2); // returns -1(not found)
# cache.put(4, 4); // evicts key 1

## Analysis
# O(1) time
# 1) data-structure=> store key and value => hashmap => store and query is O(1)
# 2) we also need to maintain the sequence, as when the cache is full, we need invalidate the least recently used item, BeFORE 
#    inserting a new item.
#    And when query occured, we should update the key, so that, we won't remove the new items unexpected.
#    => linked list, but the linked list insert and remove is too complicated.
#    => how to reduce it? => hash store the previous node. => maintain a head and tail.

## Solution
class LinkedNode(object):
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = LinkedNode()
        self.tail = self.head
        self.nodepos = {}
    
    # check exist
    # exist => update linked list, head and tail may be changed; update hash table
    # not exist => not full=> append new to the tail, update hashtable
    #           => full => remove the tail, append the new, update hashtable
    
    def put(self, key, value):
        if key in self.nodepos:
            # put involves new value update.
            self.pushahead(key, value)
            return
        if len(self.nodepos) == self.capacity:
           
            # remove the least recently used item
            pretail = self.nodepos[self.tail.key]
            del self.nodepos[self.tail.key]
            pretail.next = None
            self.tail = pretail
        # we should PUT THE NEW TO THE HEAD BUT NOT TAIL
        # append the new to the HEAD
        # BUT HOW About a empty head?
        newnode = LinkedNode(key, value)
        if not self.head.next:
            self.head.next = newnode
            self.tail = newnode
        else:
            # update newnode to previous node in hashtable
            newnode.next = self.head.next
            self.nodepos[self.head.next.key] = newnode 
            self.head.next = newnode
        self.nodepos[key] = self.head
            
 
    # check exist
    # not exist: return -1
    # exist => update list, update hashtable, return the value
    def get(self, key):
        if key not in self.nodepos:
            return -1
        self.pushahead(key)
        return self.head.next.value 

    # both get, put operation may cause the list move to the head, so we make it a seperate modulei
    # @return: None
    # @params: key - to push ahead
    # actually two cases, the key is the tail or in the middle
    def pushahead(self, key, value=None):
        if key not in self.nodepos:
            return
        npre = self.nodepos[key]
        if self.tail.key == key:
            npre.next = None
            node = self.tail
            self.tail = npre
        else: 
            # update linked list
            # 1) seperate the node from the original postion
            node = npre.next
            npre.next = node.next
            # as the node post changed its pre, therefore, we also need update its pre
            self.nodepos[node.next.key] = npre
        # 2) re-link the node to the head
        # as the previous head post changed, we also need update its hash value
        self.nodepos[self.head.next.key] = node
        node.next = self.head.next
        self.head.next = node
        # 3) update hashtable
        self.nodepos[key] = self.head 
        # 4) update node value if necessary
        if value:
            node.value = value       

if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    #print(cache.nodepos.keys())
    cache.put(3, 3)
    cache.put(3, 5)
    cache.put(4, 4)
    if cache.get(2) == -1 and cache.get(1) == -1 and cache.get(3) == 5 and cache.get(4) == 4:
        print("Passed: LRU Cache")
    else:
        print("Failed: LUR Cache")

