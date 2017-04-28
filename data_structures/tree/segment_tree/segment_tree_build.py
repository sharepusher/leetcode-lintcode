## Reference
# http://www.lintcode.com/en/problem/segment-tree-build/

## Tags - Medium
# Binary Tree; Segment Tree

## Description
# The structure of Segment Tree is a binary tree which each node has two attributes start and end,
#  denote an segment/interval.
# start and end are both integers, they should be assigned in following rules:
# 1) The root's start and end is given by build method.
# 2) The left child of node A has: start=A.left, end = (A.left + A.right) // 2
# 3) The right child of node A has: start(A.left+A.right) // 2+1, end=A.right
# 4) if start equals to end, there will be no children for this node. - BASE CASE
# Implement a build method with two parameters start and end. 
# So that we can create a corresponding segment tree with every node has the correct start and end value
# return the root of this segment tree.

## Clarification
# Segment Tree (a.k.a Interval Tree) is an advanced data structure which can support queries like
# 1) which of these intervals contain a given point
# 2) which of these points are in a given interval

## Analysis
# The segment tree is used to handle interval/range queries
# It's a binary tree with (start, end) denoting an segment/interval.
# Additionally, the Segment Tree build has no relationship with the array, but only related to the indexes
# And the build process is only about start, end indexes.
# How to build a binary/segment tree?
# by recursion - accroding to the defination of tree
# 1) prepare the tree node.
# 2) build root, left, and right

## Solution
# segment tree node prepare
class SegmentTreeNode:
    def __init__(self, start, end):
        self.start, self.end = None, None
        self.left, self.right = None, None

# @Param start, end: Denote an segment/interval
# @return: the root of Segment Tree
class Solution:
    # recursion - divide and conquer
    def build(self, start, end):
        if start > end:
            return None
        root = SegmentTreeNode(start, end)
        if start == end:
            return root
        # start < end
        # setup left and right respectively
        # the relationship between root, left and right are the connections to setup the tree
        root.left = self.build(start, (start+end)//2)
        root.right = self.build((start_end)//2 + 1, end)
         
        return root
   
