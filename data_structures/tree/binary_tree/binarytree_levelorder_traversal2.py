## Reference
# http://www.lintcode.com/en/problem/binary-tree-level-order-traversal-ii/


## Tags - Medium
# Binary Tree; Breadth First Search; Binary Tree Traversal;
# Queue


## Description
# Given a binary tree, return the bottom-up level order traversal of its nodes' values.
# (ie. from left to right, level by level from leaf to root)


## Analysis
# last problem is top-down; this one is bottom-up.
# input - the root of the binary tree
# output - the node values list from leaf to root
# The first/direct solution is the dfs max depth one, as which is similar to the previous problem
# and only need to reverse the max depth number, but how could we know the max depth
# so actually, we can figure out the solution according to previous solution,
# and then reverse the result. Any better solution? 

# Time - O(N); Space - O(N) as using extra queue or extra tempstack for reverse


## Solution
# binary tree definition
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = 0, 0

class Solution:
    # DFS for BFS
    def dfs(self, root, depth, max_depth):
        if not root or depth > max_depth:
            return []
        if depth == max_depth:
            return [root.val]
        left = self.dfs(root.left, depth+1, max_depth)
        right = self.dfs(root.right, depth+1, max_depth)
        return left+right

    def levelOrderBottom2(self, root):
        if not root:
            return []
        result = []
        max_depth = 0
        while True:
            # current depth
            depth = 0
            level = self.dfs(root, depth, max_depth)
            if not level:
                break
            result.append(level)
            max_depth += 1
        return reversed(result)


    # One queue BFS
    def levelOrderBottom1(self, root):
        if not root:
            return []
        result = []
        from collections import deque
        q = deque([root])
        while q:
            level = []
            qlen = len(q)
            for i in xrange(qlen):
                current = q.popleft()
                leve.append(current.val)
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
            result.append(level)
        newresult = []
        # reverse the result to meet the requirement
        while result:
            newresult.append(result.pop())
        return newresult


