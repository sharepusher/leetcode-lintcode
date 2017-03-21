## Reference
# http://www.lintcode.com/en/problem/segment-tree-query/


## Tags - Medium
# Segment Tree; Binary Tree


## Description
# For an integer array(index from 0 to n-1, where n is the size of this array)
# in the corresponding Segment Tree, each node stores an extra attribute max to denote the maximum number
# in the interval of the array(index from start to end)
# Design a query method with three parameters: root, start, and end
# find the maximum number in the interval[start, end] by the given root of segment tree.


## Analysis
# input - the root of segment tree
#   and the start, end of segment/interval; 
# output - The maximum number in the interval[start, end]
# after building the segment max tree
# query should be the next operation
# How to query the segment tree?
# binary search ?
# how to use the segment tree to query range ?
# we know the interval(start, end, ), and segment tree root, traverse the tree?
# binary search?
# 1) if start > middle, it's in the right part
# 



## Solution
# definition of segment Tree
class SegmentTreeNode:
    def __init__(self, start, end, count):
        self.start, self.end, self.count = start, end, count
        self.left, self.right = None, None
class Solution:
    def query(self, root, start, end):
        if not root or :
            return None
        import sys
        maximum = self.helper(root, start, end)
        if maximum == -sys.maxint or maximum == None:
            return None
        return maximum

    def helper(self, root, start, end):
        if not root:
            return None
        # out of range
        if start > root.end or end > root.start:
            return -sys.maxint
        # in the range
        if root.start >= start and root.end <= end:
            return root.max
        # left max
        left = self.helper(root.left, start, end)
        right = self.helper(root.right, start, end)
        return max(left, right)


