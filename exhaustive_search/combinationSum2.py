## Reference
# 40 https://leetcode.com/problems/combination-sum-ii/#/description
# http://www.lintcode.com/en/problem/combination-sum-ii/

## Tags - Medium
# Backtracking; DFS

## Description
# Given a collection of candidate numbers(C) and a target number(T), find all unique combinations
# in C where the candidate numbers sums to T.
# Each number in C may only be used once in the combination.
# NOTICE:
# 1) All numbers including target will be positive integers.
# 2) Elements in a combination(a1, a2..ak) must be in non-descending order.
# 3) The solution set must not contain duplicate combinations.
# Example:
# Given candidate set [10, 1, 6, 7, 2, 1, 5] and target 8.
# A solution set is:
# [
#   [1,7],
#   [1,2,5],
#   [2,6],
#   [1,1,6]
# ]

## Analysis
# sort first
# similar to subset, as the combination can only go forward but not backward
# the sum of 1,3,4 or 4,3,1 is the same for a target 

## Solutions
class Solution:
    # @params: list of candidates numbers; target number
    # @return: all the combinations that sum to target
    def combinationSum2(self, candidates, target):
        if not candidates or target is None:
	    return []
	result = []
        # Have to sort first, as combinations must be in non-descending order;
        # and simplify the duplicates filter
        candidates.sort()
        #visited = [False] * len(candidates)
	self.dfshelper(candidates, 0, target, [], result)
	return result
    def dfshelper(self, candidates, sindex, target, combination, result):
	# base case
        if target < 0:
	    return 
	if target == 0:
	    result.append([]+combination)
        
	for i in xrange(sindex, len(candidates)):
            if i != sindex and candidates[i-1] == candidates[i]:
	        continue
	    combination.append(candidates[i])
	    self.dfshelper(candidates, i+1, target-candidates[i], combination, result)
	    combination.pop() 
        
if __name__ == "__main__":
    ans = Solution()
    nums = [10,1,6,7,2,1,5]
    target = 8
    result = ans.combinationSum2(nums, target)
    if result == [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]:
	print("Passed: Combination sum2.")
    else:
	print("Failed: Combination sum2.")

