## Reference
# 515 https://leetcode.com/problems/find-largest-value-in-each-tree-row/#/description


# Tags - Medium
# BFS; DFS; BinaryTree


## Description
# You need to find the largest value in each row of a binary tree.
# Input: 
#          1
#         / \
#        3   2
#       / \   \  
#      5   3   9 
# Output: [1, 3, 9]


## Analysis
# input - root of the binary tree
# output - list of largest
# The basic way is BFS and find max of each row
# 1) get all the items of row, and use max method
# 2) maitain a largest temp variable, and compare it with each item


## Solution
# definition of binary tree.
class TreeNode(Object):
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
import sys 
class Solution(Object):
    # BFS: while + queue
    # non-recusion
    def largestValues1(self, root):
        if not root:
            return []
        result = []
        from collectons import deque
        q = deque([root])
        while q:
            largest = -sys.maxint
            qlen = len(q)
            for i in xrange(qlen):
                node = q.popleft()
                largest = max(largest, node.val)
                # update q
                for subtree in (node.left, node.right):
                    if subtree:
                        q.append(subtree) 
            result.append(largest)
        return result

    # DFS: a max level to make sure the deepest the traverse can reach.
    # in this case, the length of the result can indicate the depth
    def largestValues2(self, root):
        if not root:
            return []
        result = []
        self.dfs(root, 0, result)
        return result
    def dfs(self, root, curr_level, result):
        if not root:
            return
        if curr_level == len(result):
            result.append(root.val)
        else:
            result[curr_level] = max(result[curr_level], root.val)
        self.dfs(root.left, curr_level+1, result)
        self.dfs(root.right, curr_level+1, result)

        


