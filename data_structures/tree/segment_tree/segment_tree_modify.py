## Reference
# http://www.lintcode.com/en/problem/segment-tree-modify/


## Tags - Medium
# Lintcode Copyright; Binary Tree; Segment Tree


## Challenge
# Do it in O(h) time, h is the height of the segment tree


## Description
# For a Maximum Segment Tree, which each node has an extra value max to store the maximum value in this node's interval.
# Implement a modify function with three parameter root, index and value to change the node's value with
# [start, end] = [index, index] to the new given value. Make sure after this change, every node in segment tree still 
# has the max attribute with the correct value.

# Analysis
# input - @param: root, The root of segment tree node 
#         @ and change the node's value with [index, index] to the new given value
# output - @return: nothing.
# The process is almost the same as the build process, we need to find the index node,
# and then update it, then update parent node accordingly


class SegmentTreeNode:
    def __init__(self, start, end, max):
        self.start, self.end, self.max = start, end, max
        self.left, self.right = None, None
class SegmentTree:
    def buildIndex(self, start, end):
        if start > end:
            return None
        # now start <= end
        root = SegmentTreeNode(start, end)
        if start == end:
            return root
         
        left = self.buildIndex(start, (start+end)//2)
        right = self.buildIndex((start+end)//2+1, end)
        root.left, root.right = left, right    

        return root

    def buildMax(self, A, start, end):
        if start > end:
            return None
        # now start <= end
        root = SegmentTreeNode(start, end, None)
        if start == end:
            root.max = A[start]
            return root
        left = self.buildMax(A, start, (start+end)//2)
        right = self.buildMax(A, (start+end)//2+1, end)
        root.left, root.right = left, right
        root.max = max(left.max, right.max)
        return root

    def modify(self, root, index, value):
        if not root:
            return
        if root.start == root.end:
            if root.start == index:
                root.max = value
            return
        # change the left value 
        self.modify(root.left, index, value)
        self.modify(root.right, index, value)
        root.max = max(root.left.max, root.right.max)
        return

# 


