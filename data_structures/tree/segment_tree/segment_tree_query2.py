## Reference
# http://www.lintcode.com/en/problem/segment-tree-query-ii/


## Tags - Medium
# Lintcode Copyright; BinaryTree; SegmentTree


## Description
# For an array, we can build a SegmentTree for it, each node stores an extra attribute "count"
# to denote the number of elements in the array, which value is between interval start and end.
# The array may not fully filled by elements.
# Design a query method with three parameters: root, start, and end. 
# Find the number of elements in the array's inverval[start, end] by the given root of value
# SegmentTree.


## Analysis
# what's the meaning of count? how to get it?


## Solution
# definition of segment Tree node
class SegmentTreeNode:
    def __init__(self, start, end, count):
        self.start, self.end, self.count = start, end, count
        self.left, self.right = None, None
    
class SegmentTree:
    # input - @param: array, start, end
    # output - @return root of the segment Tree
    # Count to denote the number of elements in the array which value is between interval start and end.
    def buildCount(self, A, start, end):
        if not A or start > end:
            return None
        # now start <= end
        root = SegmentTreeNode(start, end, 0)
        if start == end:
            if A[start] == start:
                root.count = 1
            return root
        # now start != end
        left = self.buildCount(A, start, (start+end)//2)
        right = self.buildCount(A, (start+end)//2+1, end)
        root.left, root.right = left, right
        root.count = left.count+right.count
        return root
    
    # @param: root of segment tree, start, and end of the segment/interval
    # @return: the count number in the interval
    def queryCount(self, root, start, end):
        if not root or start > end:
            return None
        # if out of the root range
        if root.start > end or root.end < start:
            return 0
        # in the range:
        if root.start > start and root.end < end:
            return root.count
        # cross the range
        left = self.queryCount(root.left, start, end)
        right = self.queryCount(root.right, start, end)
        return left + right


            
         
           
    
