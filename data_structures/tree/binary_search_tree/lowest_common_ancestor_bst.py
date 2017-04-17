## Reference
# 235 https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/#/description

## Tags - Easy
# BST

## Description
# Given a binary search Tree, find the lowest common Ancestor(LCA) of two given nodes in the BST.
# According to the definition of LCA: The lowest common ancestor is defined between two nodes v and w
# as the lowest node in T that has both v and w as desenddants.
# where we allow a node to be a descendant of itself.

# Analysis
# According to the definition of BST, we know that left.val < root.val < right.val
# therefore, we can know whether the p and q are located at both sides of one side.

## Solutions
# definition of binary tree node
class TreeNode(Object):
    def __init__(val):
	self.val = val
	self.left, self.right = None, None
class Solution(Object):
    # divide and conquer
    # suppost p.val < q.val
    def lowestCommonAncestor(self, root, p, q):
	if not root:
	    return None
	if p.val < root.val < q.val or q.val < root.val < p.val:
	    return root
	# now p and q are in the same side
        if root == p or root==q:
	    return root	
	if p.val < root.val:
	    # they are in the left subtree
	    return self.lowestCommonAncestor(root.left, p, q)
	else:
	    return self.lowestCommonAncestor(root.right, p, q)

