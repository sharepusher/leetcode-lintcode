## Reference
# http://www.lintcode.com/en/problem/balanced-binary-tree/
# 110 https://leetcode.com/problems/balanced-binary-tree/#/description

## Tags - Easy
# Balanced BinaryTree; Divide and conquer; Recursion

## Description
# Given a binary tree, determin if it is height-balanced.
# For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees
# of every node never differ by more than 1.

## Analysis
# input - the root of binary tree
# output - True if the binary tree is balanced.
# The key of this problem:
# 1) the balanced binary tree requires that all it's subtrees should be balanced
#    in other words, it's easier to be proved by recursion. 
# 2) the balanced condition is that abs(left height -right height) <= 1
#    in other words, we need to know the max depth of subtrees, and compare the left and right max depth

## Solution
# definition of bianry tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def isBalanced2(self, root):
        if not root:
            return True
        balanced, _ = self.depth(root)
        return balanced

    def depth(self, root):
        if not root:
            return True, 0
        lbalanced, left = self.depth(root.left)
        rbalanced, right = self,depth(root.right)
        balanced = abs(left-right) <= 1 and lbalanced and rbalanced
        maxdepth = max(left, right) + 1
        return balanced, maxdepth

    def isBalanced1(self, root):
        # corner case
        if not root:
            return True
        return self.maxDepth(root) != -1
    # 1) calculate the max height of tree
    # 2) return max depth of the tree
    # 3) return -1 if the subtree is not balanced.
    def maxDepth(self, root):
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        if abs(left-right) > 1 or left == -1 or right == -1:
            return -1
        return max(left, right) + 1 
        
