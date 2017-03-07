## Reference
# http://www.lintcode.com/en/problem/segment-tree-build-ii/

## Tags - Medium
# Segment Tree

## Description
# The structure of Segment Tree is a binary tree which each node has two attributes 
# start and end denote an segment/interval.
# start and end are both integers, they should be assigned in following rules:
# 1) The root's start and end is given by build method.
# 2) The left child of node A has: start = A.left, end = (A.left+A.right) // 2
# 3) The right child of node A has: start = (A.left + A.right)//2 + 1, end = A.right
# 4) if start equals to end, there will be no children for this node.
# Implement a build method with a given array, so that we can create a corresponding 
# segment tree with every node value represent the corresponding interval max value in the array,
# return the root of this segment tree.

## Clarification
# Segment Tree(a.k.a Interval Tree) is an advanced data structure which can support queries
# 1) which of these intervals contain a given point
# 2) which of these points are in a given interval

# Compared with the first version of Segment tree
# The segment tree in this version should include max to indicate the max element in the interval

## Analysis
# According to problem, there are many kinds of segment tree, which are all based on the basic
# start, end, but including other items required.
# here, we need include the "max" element in the segment tree node, to indicate the 
# max element in the range

# There are two points:
# 1) one is we need re-define the segment tree to include the max element
# 2) the other is how we know the max value when build the segment Tree.
# About the second question, as the original list is unsorted,
# and we cannot sort it, as we need to keep it in the original order  

# as the recursion tree will go deep to the end first, in this case, we will know left and right node, 
# we can get the left and right, then compare them, and update the root, then
# How to build the segment Tree:
# recursion - pre-order traversal; divide and conquer
#


## Solution
# Definition of Segment Tree Node

class SegmentTreeNode:
    def __init__(self, start, end, max)
        start, end, max = None, None, None
        left, right = None, None

class Solution:
    # @param A: a list of integer
    # @return The root of Segment Tree

    def buildMax(self, start, end, A):
        if start > end:
            return None
        max_node = A[start]
        root = SegmentTreeNode(start, end, max_node)
        if start == end:
            return root
        ## start < end
        root.left = self.buildMax(start, (start+end)//2, A)
        root.right = self.buildMax((start+end)//2+1, end, A)
        # conquer
        if root.left and root.left.max > root.max:
            root.max = max(left.max, right.max)
        if root.right and root.right.max > root.max:
            root.max = root.right.max
        return root

    def build(self, A):
        if not A:
            return None
        N = len(A)
        start, end = 0, N-1
        return self.buildMax(start, end, A)


