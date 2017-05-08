## Reference
# http://www.lintcode.com/en/problem/subsets/#
# 78 https://leetcode.com/problems/subsets/#/description

## Tags - Medium - Blue
# Array; Backtracking; Bit Manipulation; Facebook; Uber

## Description
# Given a set of DISTINCT integers, nums, return all possible subsets.
# NOTE: The solution set must not contain duplicate subsets.

# For example, 
# If nums = [1, 2, 3], a solution is:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
# 

## Challenge
# Can you do it in both recursively and iteratively?

## Solutions
class Solution(object):
    def subsets(self, nums):
	if nums == None:
	    return []
	result = []
	self.helper(nums, 0, [], result)
	return result
    # collect subset and put in result
    def helper(self, nums, start_idx, subset, result):
	result.append([] + subset)
	for i in xrange(start_idx, len(nums)):
	    subset.append(nums[i])
	    self.helper(nums, i+1, subset, result)
	    del subset[-1]

if __name__ == "__main__":
    nums = [1, 2, 3]
    


