## Reference
# http://www.lintcode.com/en/problem/construct-binary-tree-from-preorder-and-inorder-traversal/#


## Tags - Medium
# BinaryTree


## Description
# Given preorder and inorder traversal of a tree, construct the binary tree.
# NOTE: you may assume that duplicates do not exist in the tree.
# Example: given in-order [1, 2, 3] and pre-order[2,1,3], return a tree:
#   2
#  / \
# 1   3


## Analysis
# input: preorder, inorder lists
# output: root node
# preorder is root,left, right; inorder is left, root, right
# the fist must be root; then we can seperate left subtree and rightsubtree
# the key is how to disthingui left and right part
# list.index(value) can return the first index of value.
# Raises ValueError if the value is not present. 


## Solution
# definition of binary tree
class TreeNode(Object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
class Solution(Object):
    # divide and conquer
    def buildTree(self, preorder, inorder):
        if not preorder:
	    return None
	root = TreeNode(preorder[0])
	rpos = inorder.index(preorder[0])
	root.left = self.buildTree(preorder[1:rpos+1], inorder[:rpos])
        root.right = self.buildTree(preorder[rpos+1:], inorder[rpos:])
        return root


