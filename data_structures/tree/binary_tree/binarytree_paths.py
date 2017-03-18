## Reference
# http://www.lintcode.com/en/problem/binary-tree-paths/


## Tags - Easy
# Binary Tree; BinaryTree Traversal; Facebook; Google


## Description
# Given a binary tree, return all root-to-leaf paths.


## Analysis
# all paths -> DFS; 
# input - the root of the binary tree;
# output - 2D list of all root to leaf paths
# as it's root to leaf? preorder traversal
# we need a temp path and then merge path to paths
# how? when go to the end, merge , go back 
# "->" the arrow is not that easy to organize, we can use list fist, and then convert it to str



## Solution
# definition of binary tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    # DFS - recursion(divide and conquer)
    def binaryTreePaths(self, root):
        paths = []
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        lpaths = self.binaryTreePaths(root.left)
        rpaths = self.binaryTreePaths(root.right)
        for path in lpaths:
            paths.append(str(root.val) + "->" + path)
        for path in rpaths:
            paths.append(str(root.val) + "->" + path)
        return paths


    # DFS - recursion(traverse)
    def binaryTreePaths2(self, root):
        if not root:
            return []
        paths = []
        self.dfsHelper2(root, str(root.val), paths)
        return paths
    def dfsHelper2(root, path, paths):
        if not root:
            return
        if not root.left and not root.right:
            # merge path to paths
            paths.append(path)
            return
        if root.left:
            self.dfsHelper2(root.left, path + "->" + str(root.left.val), paths)
        if root.right:
            self.dfsHelper2(root.right, path + "->" + str(root.right.lva), paths)
        


    def binaryTreePaths1(self, root):
        if not root:
            return []
        paths = []
        path = []
        self.dfsHelper(root, path, paths)
        return paths
    # put path to paths
    def dfsHelper(self, root, path, paths):
        if not root:
            return
        path.append(str(root.val))
        if not root.left and not root.right:
            # merge path to paths
             
            paths.append("->".join(path))
        # put root.left path to paths
        self.dfsHelper(root.left, path, paths)
        self.dfsHelper(root.right, path, paths)
        path.pop()
        




