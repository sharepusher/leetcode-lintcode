## Reference
# http://www.lintcode.com/en/problem/invert-binary-tree/


## Tags - Easy
# Binary Tree; DFS


## Description
# Invert a binary tree


## Challenge
# Do it in recursion is acceptable, can you do it without recursion



## Analysis
# Invert means making an inversion; reverse the position, order, relation, or conditon of
# turn inside out or upside down, here is turn left to right, and right to left.
#
# the intuitive solution is clone the left and right, then replace the root left and root right with reverse order.
# It's WRong, as actually, the invert means, each subtree has to be inverted, but not the main subtree of root
# which means, we have to think about it with recursion first. 
# 
# input - the root of the binary tree
# ouput - NOTHING, as the root won't change, only left and right subtree are exchanged.
#


## Solution
# definition of binary tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    # DFS - recursion
    def invertBinaryTree1(self, root):
        if not root:
            return
        # exchagne the left and right of root
        root.left, root.right = root.right, root.left
        # revert left subtree
        self.invertBinaryTree(root.left)
        self.invertBinaryTree(root.right)

    # non-recurison - stack
    def invertBinaryTree(self, root):
        if not root:
            return 
        stack = [root]
        while stack:
            current = stack.pop()
            current.left, current.right = current.right, current.left
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)


