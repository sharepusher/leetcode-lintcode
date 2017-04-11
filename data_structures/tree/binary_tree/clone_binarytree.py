## Reference
# http://www.lintcode.com/en/problem/clone-binary-tree/

## Tags - Easy
# Binary Tree; DFS; Divde and conquer


## Description
# For the given binary tree, return a DEEP COPY of it.


## Analysis
# input - @param: the root of a binary tree
# output - @return root of the new tree

# 1) deep copy should copy the node value and node relationship
# 2) copy root first, and then left, right => pre-order traversal;
# return the new binary tree with same structure and same value.
# create new node and traverse
# divide and conquer is better 


## Solution
# definition of binary tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    # DFS - nonrecursion: stack
    def cloneTree2(self, root):
        if not root:
            return None
        # as we need a newroot, and keep the new root updated together with original one
        # so we need put both of them into the stack
        # Update the deep copy node when stack pop up, as we need do other node copy in the while loop
        newroot = TreeNode(None)
        stack = [(root, newroot)]
        while stack:
            node, newnode = stack.pop()
            newnode.val = node.val
            if node.left:
                newnode.left = TreeNode(None)
                stack.append((node.left, newnode.left))
            if node.right:
                newnode.right = TreeNode(None)
                stack.append((node.right, newnode.right))
        return newroot


    
    # DFS - recursion:divide and conquer
    def cloneTree1(self, root):
        if not root:
            return None
        # clone root value
        newroot = TreeNode(root.val)
        # clone left subtree
        left = self.cloneTree(root.left)
        # clone right subtree
        right = self.cloneTree(root.right)
        # merge left and right to root
        newroot.left, newroot.right = left, right
        return newroot


