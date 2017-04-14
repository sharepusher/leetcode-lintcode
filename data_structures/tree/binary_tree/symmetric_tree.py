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
    # BFS: while+queue(deque)
    def isSymmetric4(self, root):
        if not root:
  	    return True
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False
        # now compare left and right subtree
    	from collections import deque
 	q1 = deque([root.left])
        q2 = deque([root.right])
        while q1 and q2:
            curr1, curr2 = q1.popleft(), q2.popleft()
            if not curr1 and not curr2:
                continue
            if not self.comNode(curr1, curr2):
                return False
            # update q1 and q2 by collecting q1.left,q1.right and q2.right,q2.left
            q1.append(curr1.left)
            q1.append(curr1.right)
            q2.append(curr2.right)
            q2.append(curr2.left)
        return True
            
    def compNode(self, node1, node2):
        if not node1 and not node2:
            return True
        if node1 and node2 and node1.val == node2.val:
            return True
        return False 
    

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

