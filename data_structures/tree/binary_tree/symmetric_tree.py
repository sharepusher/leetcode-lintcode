## Reference
# https://leetcode.com/problems/symmetric-tree/#/description



## Tags - Easy
# Binary Tree; DFS; BFS


## Description
# Given a binary tree, check whether it is a mirror of itself.
# i.e., symmetric around its center.
# For example, binary tree [1, 2, 2, 3, 4, 4, 3] is symmetric.
# But the following [1, 2, 2, null, 3, null, 3] is not.


## Challenge
# both Recursively and Iteratively.



## Solution
# definition of binary Tree
class TreeNode(Object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = left, right
   
class Solution:
    # DFS - recursion: divide and conquer
    def isSymmetric3(self, root):
        if not root:
            return True
        return self.helper(root.left, root.right)
    # compare node1 and node2
    def helper(self, root1, root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        return self.helper(root1.left, root2.right) and self.helper(root1,right, root2.left)

    def isSymmetric1(self, root):
        if not root:
            return True
        return self.dfs(root.left, False) == self.dfs(root.right, True)
    # dfs will traverse and collect nodes values
    # input - root, flag to indicate whether it's traversed by 'root', 'right', 'left'
    def dfs(self, root, flag):
        if not root:
            return ['#']
        left = self.dfs(root.left, flag)
        right = self.dfs(root.right, flag)
        if flag:
            return [root.val] + right + left
        return [root.val] + left + right

    # DFS: non-recursion(while+stack)
    # empty node return '#'
    def isSymmetric2(self, root):
        if not root:
            return True
        return self.dfshelper(root.left, False) == self.dfshelper(root.right, True)
    def dfshelper(self, root, flag):
        if not root:
            return []
        result = []
        stack = [root]
        while stack:
            current = stack.pop()
            if current:
                result.append(current.val)
            else:
                result.append('#')
                continue
            # update stack
            if flag:
                seq = (root.right, root.left)
            else: 
                seq = (root.left, root.right)
            for node in seq:
                if node:
                    stack.append(node)
                else:
                    stack.append(None)
        return result    

