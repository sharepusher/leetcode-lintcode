## Reference
# http://www.lintcode.com/en/problem/identical-binary-tree/


## Tags - Easy
# Binary Tree; DFS; Divide and conquer; Recursion


## Description
# Check if two binary trees are identical. Identical means the two binary trees have the same structure
# and every identical position has the same value.


## Analysis
# Input - root node of binary tree A, root node of binary tree B
# output - True if they are identical, or False

# is it like the clone ?
# not only the node value, but also the position should be the same
# There are two ways to make it:
# 1) Time-O(N), Space-O(N): the initla idea was using the list to repsent array, 
#    and compare the list, that's why the space is O(N)# 2)
# 2) Time-O(N), Space-O(1): according to the binary tree definition, traverse the binary tree and compare it one by one.
# 


## Solution
# definition of binary tree
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    def isIdentical1(self, a, b):
        # conver the tree to list
        # how ? there should be convert function
        atree = self.convertToList(a)
        btree = self.convertToList(b)
        return atree == btree
    # DFS: preorder traverse - recursion(divide and conquer) 
    def convertToList(self, root):
        if not root:
            return ["#"]
        left = self.convertToList(root.left)
        right = self.convertToList(root.right)
        return [root.val] + left + right
    
    # DFS - preorder Traverse; recursion
    def isIdentical2(self, a, b):
        if not a and not b:
            return True
        if a and b and a.val == b.val:
            return self.isIdentical2(a.left, b.left) and \
            self.isIdentical2(a.right, b.right)
        return False
    def isIdentical3(self, a, b):
        if not a and not b:
            return True
        if (not a and b) or (not b and a) or a.val != b.val:
            return False
        # now a and b are identical, we need check left and right
        return self.isIdentical3(a.left, b.left) and self.isIdentical3(a.right, b.right)





