## Reference
# http://www.lintcode.com/en/problem/subtree/#


## Tags - Easy
# Binary Tree; DFS; Recursion


## Description
# You have two every large binary trees: 
# T1, with millions of nodes, and T2, with hundreds of nodes,
# Create an algorithm to decide if T2 is a subtree of T1

# Notice: A tree T2 is a subtree of T1 if there exists a node n in T1
# such that the subtree of n is identical to T2.
# That is, if you cut off the three at node n, the two trees would be identical.


## Analysis
# larget binary tree? does it imply that we should use non-recursion
# input - the root of T1, T2  
# output - True if T2 is a subtree of T1, or False
# It's DFS, as we need traverse all the nodes to check whether there's some equals to T2's node
# first, travese to find T2's node
# second, use the previous identical problem solution to validate it.
# Therefore, it's time complexity is O(M*N), M is the time to find the T2's node



## Solution
# definition of binary tree
def TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def Solution:
    # recursion + recursion
    def isSubtree3(self, T1, T2):
        if not T2:
            return True
        if not T1:
            return False
        # now both T1 and T2 are True
        if T1.val == T2.val:
            if self.identical(T1, T2):
                return True
        # continue the traverse even the identical failed
        # check left subtree
        left = self.isSubtree(T1.left, T2)
        right = self.isSubtree(T1.right, T2)
        return left or right
    def isSubtree2(self, T1, T2):
        if not T2:
            return True
        # when traverse to the end, no T2 found, we should return False
        if not T1:
            return False
        return self.identical(T1, T2) or self.isSubtree2(T1.left, T2) or self.isSubtree(T1.right, T2)
        


    # DFS: non-recursion(stack) + recursion
    # traverse to find T2
    # how? DFS check node by node
    # and continue the traverse when validation failed !! IT's very IMPORTANT
    # As there's duplicated nodes that may be the same as the root of T2
    def isSubtree1(self, T1, T2):
        if not T2:
            return True
        # now T2 is True
        if not T1:
            return False
        stack = [T1]
        while stack:
            T1 = stack.pop()
            if T1.val == T2.val and self.identical(T1, T2):
                return True
            if T1.right:
                stack.append(T1.right)
            if T1.left:
                stack.append(T1.left)
        # traverse finished, no match found
        return False
    # DFS - recursion(divide and conquer)            
    def identical(self, a, b):
        if not a and not b:
            return True
        if a and b and a.val == b.val:
            left = self.identical(a.left, b.left)
            right =self.identical(a.right, b.right)
            return left and right
        return False
            
      
