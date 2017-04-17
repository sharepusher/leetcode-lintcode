## Reference
# 108 https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/#/description
# http://www.lintcode.com/en/problem/convert-sorted-array-to-binary-search-tree-with-minimal-height/

## Tags - Easy
# DFS

## Description
# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

## Analysis
# KEY: 1) height balanced 2) bst list is sorted, so the middle is the root, and then can be height balanced.

## Solution
# definition of binary tree.
class TreeNode(Object):
    def __init__(self, val):
        self.val = val
	self.left, self.right = None, None
class Solution(Object):
    # Divide and conquer
    def sortedArrayToBST1(self, nums):
        if not nums:
	    return None
	middle = len(nums) // 2
	root = TreeNode(nums[middle])
	root.left = self.sortedArrayToBST1(nums[:middle])
	root.right = self.sortedArrayToBST1(nums[middle+1:])
	return root

    def sortedArrayToBST2(self, nums):
	if not nums:
	    return None
	# KEY: len(nums)-1, but not len(nums), as we are using indeX
	return self.helper(nums, 0, len(nums)-1)
    def helper(self, nums, start, end):
	if start > end:
	    return None
	if start == end:
	    return TreeNode(nums[start])
	middle = (start+end) // 2
	root = TreeNode(nums[middle])
	root.left = self.helper(nums, start, middle-1)
	root.right = self.helper(nums, middle+1, end)
	return root



