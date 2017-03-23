## Reference
# http://www.lintcode.com/en/problem/interval-sum-ii/

## Tags - Hard
# Lintcode Copyright; Segment Tree

## Challenge
# O(logN) time for query and modify


## Description
# Given an integer array in the construct method, implement two methods query(start, end)
# and modify(index, value):
# 1) For query(start, end), return the sum from index start to index end in the given array
# 2) For modify(index, value), modify the number in the given index to value
# Given array A = [1, 2, 7, 8, 5].
# query(0, 2), return 10; modify(0, 4), change A[0] from 1 to 4.


## Analysis
# set up and build segment tree for the query and modify
# The setup process is O(N) time and O(N) space; while the query and modify is O(logN) time

## Solution
# definition of segment sum tree, and build, qery, modify interface
class SegmentTree:
    def __init__(self, start, end, isum):
        self.start, self.end, self.isum = start, end, isum
        self.left, self.right = None, None
    # API for build
    # @params: A, start, end
    # @return: the root of the segment tree
    @classmethod
    def build(cls, A, start, end):
        # corner case
        if not A:
            return None
        # init root node
        root = SegmentTree(start, end, A[start])
        # base case
        if start == end:
            return root
        left = cls.build(A, start, (start+end)//2)
        right = cls.build(A, (start+end)//2+1, end) 
        root.left, root.right = left, right
        root.isum = left.isum + right.isum
        return root

    # API for query
    # @params: the interval, and DO NOT forget the root of the segment tree
    #     which is the entrance of the query process.
    # @return: the sum of the interval
    @classmethod
    def query(cls, root, start, end):
        # corner case
        if not root:
            retur None
        # out of the range
        if root.start > end or root.end < start:
            return 0
        # in the range
        if root.start >= start and root.end <= end:
            return root.isum
        # cross the range
        left = cls.query(root.left, start, end)
        right = cls.query(root.right, start, end)
        return left+right

    # API for modify
    # @params: root of the segment tree, index and value to be updated
    # @return: nothing
    @classmethod
    def modify(cls, root, index, value):
        if not root:
            return
        # root is leaf, the end
        if root.start == root.end:
            if root.start == index:
                root.isum = value
            return
        # now root is not leaf, it has left and right node
        if root.left.end >= index:
            cls.modify(root.left, index, value)
        else:
            cls.modify(root.right, index, value)
        root.isum = root.left.isum + root.right.isum

class Solution:
    # @param: A, the integer list
    def __init__(self, A):
        # build and init a global variable 
        self.root = SegmentTree.build(A, 0, len(A)-1)
    # @param: indices
    # @return: sum
    def query(self, start, end) 
        if not root or start > end:
            return None
        return SegmentTree.query(self.root, start, end)

    # @param: index, value
    # @return: nothing
    def modify(self, index, value):
        if not root:
            return
        SegmentTree.modify(sefl.root, index, value)
             

            
