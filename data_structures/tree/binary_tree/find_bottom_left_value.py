## Reference
# 513 https://leetcode.com/problems/find-bottom-left-tree-value/#/description

## Tags - Medium
# BinaryTree; DFS; BFS

## Description
# Given a binary tree, find the leftmost value in the last row of the tree.

# Example:
# input 213, output1

## Analysis
# DFS: while + stack
# binary tree => divide and conquer: how about the left subtree; how about right subtree
# how about their relationship.
# we need to compare left, right subtree level, therefore, there should be a helper
# to return level and value, and at the same time, we need maintain level during dfs

# BFS: while + queue(deque)
# we should maintain a leftvalue, and we needn't keep others
# but just make sure the first value of the level will be updated, others won't
# AND be careful that, the left value may be 0. Therefore, pay attention to 
# the judegement when checking its existence.


## Solution:
# definition of binary tree
class TreeNode(Object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution(Object):
    # DFS: recursion(divide and conquer)
    # @params: root of the binary tree
    # @return: left most value
    def findBottomLeftValue1(self, root):
        # corner case
        if not root:
            return None
        _, val = self.dfshelper(root, 0)
        return val
    # @params: root of the binary tree; level of current root
    # @return: left most level and value 
    def dfshelper(self, root, level):
        # base case
        if not root:
            return -1, None
        if not root.left and not root.right:
            return level, root.val
        # divide and conquer
        llevel, lval = self.dfshelper(root.left, level + 1)
        rlevel, rval = self.dfshelper(root.right, level + 1)
        if llevel >= rlevel:
            return llevel, lval
        return rlevel, rval

    # BFS: while + queue(deque)
    def findBottomLeftValue2(self, root):
        if not root:
            return None
        from collections import deque
        q = deque([root])
        result = root.val
        while q:
            leftval = None
            qlen = len(q)
            for i in xrange(qlen):
                current = q.popleft()
                if leftval is None:
                    leftval = current.val
                seq = (current.left, current.right)
                for node in seq:
                    if node:
                        q.append(node)
            result = leftval
        return result



