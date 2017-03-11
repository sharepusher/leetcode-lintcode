## Reference
# http://www.lintcode.com/en/problem/binary-tree-inorder-traversal/


## Tags - Easy; Medium(non-recursion)
# DFS; BinaryTree; Recursion; BinaryTree Traversal


## Challenge
# Do it without recursion

## Description
# Given a binary tree, return the inorder traversal of its nodes' value.


## Analysis
# input - root node of the binary tree
# output - a list of node value(all the node value)
# All solution - DFS
# preorder traversal; inorder traversal; postorder traversal
#
# The NON-recursion of in-order is different from the one of pre-order traversal !
# The inorder traversal needs to record the left node, then the root, and finally the right
# so two steps for non-recursion
# while root or stack
# 1) enqueue left node to stack until the left end;
# 2) pop up and enqueue the right to the stackk
# in other words, as we wanna pop up the left, when no left, we can pop it directly and check whether that node has right
# if have, enqueue the right

#Time - O(N): each node will be visited in linear times; no extra space if it's recursion
#  

## Solution
# Defination of Binary Tree Node
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self. right = None, None

class Solution:
    ## non-recursion ******** 
    def inorderTraversal1(self, root):
        result = []
        if not root:
            return result
        stack = []
        # we do NOT use root.left, as we also need to handle root.right
        # or it would be a little bit complex
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                result.append(root.val)
                root = root.right
        return result
    ## recursion
    # divide and conquer
    # result in return
    def inorderTraversal2(self, root):
        if not root:
            return []
        # left part traversal
        left = self.inorderTraversal2(root.left)
        right = self.inorderTraversal2(root.right)
        return left + [root.val] + right
    ## recursion
    # traverse
    # result in parameter
    def inorderTraversal3(self, root):
        if not root:
            return []
        result = []
        self.dfshelper(root, result)
        return result
    def dfshelper(self, root, result):
        if not root:
            return
        # put the left part in result
        self.dfshelper(root.left, result)
        result.append(root.val)
        self.dfshelper(root.right, result)

        
            
        



    ## recursion
    # divide and conquer
    def inorderTraversal1(self, root):
        if not root:
            return []
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)
        return left + [root.val] + right

    ## recursion - traverse
    # as traverse does not return result, but include the result in input parameter, 
    # so we need a recursion helper to make it
    def inorderTraversal2(self, root):
        if not root:
            return []
        result = []
        self.dfshelper(root, result)
        return result
        
    def dfshelper(self, root, result):
        if not root:
            return
        self.dfshelper(root.left, result)
        result.append(root.val)
        self.defshelper(root.right, result)
    
