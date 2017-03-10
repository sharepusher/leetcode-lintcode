## Reference
# http://www.lintcode.com/en/problem/binary-tree-level-order-traversal/


## Tags - Easy
# BFS; Binary Tree; Binary Tree Traversal; Queue; Linkedin; Facebook; Uber



## Challenge
# 1. Using only 1 queue to implement it.
# 2. Use DFS algorithm to do it


## Description
# Given a binary tree, return the level order traversal of its nodes' values.
# i.e., from left to right, level by level



## Analysis
# input - root of the binary tree
# ouput - a 2D lit that in level order
# Data structure:
#     DFS - stack; BFS - queue
# for BFS, one problem is when to push data to the queue, when to pop(0) - use queue
# the second is how to output and distinguish the data level by level in 2D matrix
# There are many ways to distinguish the levels:
# 1) two queues: traverse one queue, and store all the other data in a new queue, and then traverse the new queue
# 2) one queue + one flag(dummy seperator)
# 3) one queue + length?
# 4) DFS
# 
# recursion ? non-recursion ? 
# BFS is easier to implement with non-recursion ??? as it's not present data in a tree style?



## Solution
# Definiton of binary tree node
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    # dfs implement bfs
    def dfs(self, root, depth, max_depth):
        if not root or depth > max_depth:
            return []
        if depth == max_depth:
            return [root.val]
        left = self.dfs(root.left, depth+1, max_depth)
        right = self.dfs(root.right, depth+1, max_depth)
        return left + right

    def levelOrder(self, root):
        if not root:
            return []
        result = []
        max_level = 0
        while True:
            current = 0
            level = self.dfs(root, current, max_level)
            if not level:
                # no more nodes
                break
            result.append(level)
            max_level += 1
        return result

    # non-recursion
    # one queue 
    def levelOrder2(self, root):
        if not root:
            return []
        result = []
        from collections import deque
        deq = deque([root])
        while deq:
            level = []
            qlen = len(deq)
            for i in xrange(qlen):
                current = deq.popleft()
                level.append(current.val)
                if current.left:
                    deq.append(current.left)
                if current.right:
                    deq.append(current.right)
            result.append(level)
        return result
         

    # two queues: one for traverse, one for temp storage 
    def levelOrder1(self, root):
        if not root:
            return []
        result = []
        from collections import deque
        deq = deque([root])
        while deq:
            level = []
            temp = []
            for node in deq:
                level.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    tmep.append(node.right)
            result.append(level)
        return result


