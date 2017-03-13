## Reference
# http://www.lintcode.com/en/problem/minimum-depth-of-binary-tree/#


## Tags - Easy
# Binary Tree; Depth First Search; Divde and conquer


## Description
# Given a binary tree, find its minumum depth.
# The minimum depth is the number of nodes alongs the shortest path from the root node down to the nearest leaf node.


## Analysis
# It is NOT the same as maximum depth of bianry tree.
# The key of this problem is to understand the meaing of leaf node!
# The topmost node of the tree is known as the root node.
# It provides the single access point into the structure.
# The root node is the only node in the tree that does not have an incoming edge.
# 
# Nodes that have at least one child as known as Interior nodes.
# while nodes that have no children are known as Leaf Nodes(leaves).
#
# i.e. when the nodes only have one child, it's just a interior but not a leaf
#  

# T - O(N) each node will be traversed; S - O(1) if system stack are not counted.

## Solution
# definition of binary tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        # if left unreachable, it's invalid path, we should go right instead, and the total is right+1
        if not left:
            return right + 1
        if not right:
            return left + 1
        # if both of left and right child are exist
        # chose the smaller one
        return min(left, right) + 1

        
          
