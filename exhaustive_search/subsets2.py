## Reference
# 90 https://leetcode.com/problems/subsets-ii/#/description

## Tags - Medium
# Array; Backtracking; 

## Description
# Given a collection of integers that might contain duplicates, nums, 
# return all possible subsets.
# NOTE: The solution set must not contain duplicate subsets.
# For example,
# If nums = [1, 2, 2], a solution is:
# [
#  [2],
#  [1],
#  [1,2,2],
#  [2,2],
#  [1,2],
#  []
# ]

## Analysis
# The difference of this problem from last one is that there's duplicate, we have to handle them properly.
# How to avoid the duplicate?
# i != start_idx and nums[i] == nums[i-1]

## Solutions
class Solution(object):
    def subsetsWithDup(self, nums):
	if nums == None:
	    return []
	result = []
	self.helper(nums, 0, [], result)
	return result
    def helper(self, nums, start_idx, subset, result):
	result.append([]+subset)
	for i in xrange(start_idx, len(nums)):
	    if i != start_idx and nums[i] == nums[i-1]:
		continue
	    subset.append(nums[i])
	    self.helper(nums, i+1, subset, result)
	    del subset[-1]


