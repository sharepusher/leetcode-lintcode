## Reference
# http://www.lintcode.com/en/problem/binary-tree-preorder-traversal/


## Tags - Easy
# BinaryTree; BinaryTree Traversal; Recursion; NonRecursion


## Challenge
# Do it WITHOUT recursion


## Description
# Given a binary tree, return the preorder traversal of its node's values.


## Analysis
# input - the root of binary tree
# output - return the list contains node values
#
# keyword - binarytree, preorder traversal
# first, the binary tree node structure
# we have to construct the binary tree node
# class BinaryTreeNode
# second, recursion and non-recursion
# Three elements of recursion:
# 1) the defination of the recursion - input; output; what does the recursion do?
# 2) the construction of the recursion
# 3) the exit of the recursion(when the recursion stop/quit)
# 


## Solution 
# Defination of Binary Tree Node.
class TreeNode:
    def __init__(self, val):
        self.val = val
        slef.left, self.right = None, None

# DFS - Depth first search - find all the solution.
class Solution:
    # Non-recursion
    # how ? stack + loop
    def preorderTraversal3(self, root):
        if not root:
            return []
        result = []
        stack = [root]
        while stack:
            node = stack.pop()
            result.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

    # recursion
    # 1) defination of the recursion:
    #     input - root, result
    #     output - return None
    #     process - traverse the tree and record the vals to the result
    # 2) how recursion: pre-order
    # 3) when to stop:
    #    no child; finish the left and right  
    def traversalRec(self, root, result):
        # base case
        if not root:
            return
        result.append(root.val)
        self.traverseRec(root.left, result)
        self.traverseRec(root.right, result) 

    def preorderTraversal1(self, root):
        if not root:
            return []
        result = []
        self.traversalRec(root, result)
        return result
    
    # divide and conquer - return result in return value
    def preorderTraversal2(self, root):
        if not root:
            return []
        left = self.preorderTraversal2(root.left)
        right = self.preorderTraversal2(root.right)
        return [root.val] + left + right

if __name__ == "__main__":
    pass
