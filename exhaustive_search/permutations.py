## Reference
# http://www.lintcode.com/en/problem/permutations/
# 46 https://leetcode.com/problems/permutations/#/description

## Tags - Medium; Yello
# Backtracking; linkedin

## Description
# Given a collection of DISTINCT numbers, return all possible permutations.
# Example:
# For nums = [1,2,3], the permutations are:
# [
#  [1,2,3],
#  [1,3,2],
#  [2,1,3],
#  [2,3,1],
#  [3,1,2],
#  [3,2,1]
# ]

## Challenge
# Do it without recursion

## Analysis
# we needn't the start_index anymore, as we know have to traverse all of the list
# BUT we need check the visited to avoid duplicate

## Solutions
class Solution(object):
    def permute(self, nums):
	if not nums:
	    return []
	result = []
	self.helper(nums, [], result)
	return result
    # generate permutation and put them to result when len(perm) == len(nums)
    def helper(self, nums, perm, result):
	# base case
	if len(nums) == len(perm):
	    result.append(perm)
	    return 
	for i in xrange(len(nums)):
	    if nums[i] in perm:
	        continue
	    perm.append(nums[i])
	    self.helper(nums, perm, result)
	    del perm[-1]

	
