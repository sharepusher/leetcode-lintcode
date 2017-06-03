## Reference
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/#/description

## Tags - Medium
# Binary Search Tree; Inorder traversal

## Description
# Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
# Note:
# You may assume k is always valid, 1 <= k <= BST's total elements
# Follow up:
# What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently?
# How would you optimize the KthSmallest routine?

## Analysis
# BST inorder traversal can get the smallest one by one.

## Solutions
class Solution(object):
    # convert bst to sorted array and then find the kth smallest
    def kthSmallest1(self, root, k):
	# corner case
	if not root or not k:
	    return None
	bst = self.convertBST(root)
	if k <= len(bst):
	    return bst[k-1]
	return None
    # recursion - divide and conquer
    def convertBST(self, root):
	if not root:
	    return []
	return self.convertBST(root.left) + [root.val] + self.convertBST(root.right)

    # find the kth smallest during the in-order traversal
    # save time and space
    # non-recursion inorder traversal
    def kthSmallest2(self, root, k):
	if not root or not k:
	    return None
	stack = []
	while stack or root:
	    # push stack and go down to left 
	    if root:
		stack.append(root)
		root = root.left
	    else:
		# pop stack and handle the value
		root = stack.pop()
		k -= 1
		if k == 0:
		    return root.val
		# handle right subtree
		root = root.right
	# failed to find the k
	return None	

