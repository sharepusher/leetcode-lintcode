## Reference
# http://www.lintcode.com/en/problem/clone-binary-tree/

## Tags - Easy
# Binary Tree; DFS; Divde and conquer


## Description
# For the given binary tree, return a DEEP COPY of it.


## Analysis
# input - @param: the root of a binary tree
# output - @return root of the new tree
# return the new binary tree with same structure and same value.
# traverse and create new node
# divide conquer? seems traverse is better than divide and conquer, as only root can be returned.
# actuall divide and conquer is better 


## Solution
# definition of binary tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def cloneTree(self, root):
        if not root:
            return None
        # clone root value
        newroot = TreeNode(root.val)
        # clone left subtree
        left = self.cloneTree(root.left)
        # clone right subtree
        right = self.cloneTree(root.right)
        # merge left and right to root
        newroot.left, newroot.right = left, right
        return newroot


## Solution



