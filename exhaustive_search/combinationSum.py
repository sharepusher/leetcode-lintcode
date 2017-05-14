## Reference
# 39 https://leetcode.com/problems/combination-sum/#/description
# http://www.lintcode.com/en/problem/combination-sum/#

## Tags - Medium; Blue
# Array; Backtracking

## Description
# Given a set of candidate numbers(C) and a target number(T), find all unique combinations
# in C where the candidate numbers sums to T.
# The same repeated number may be chosen from C unlimited number of times.
# NOTICE:
# All numbers including target should be positive.
# Elements in a combination(a1..ak) must be in non-descending order(ie.a1 <= a2... <=ak)
# The solution set must not contain duplicate combinations
# Example:
# Given candidate set[2,3,6,7], and target 7, a solution set is:
# [[7], [2,2,3]]

## Analysis
# 1) corner case: target > 0; 
# 2) sort can make it easier to combine

## Solution
# O(N!) time ; O(N) space
class Solution(object):
    def combinationSum(self, candidates, target):
	# corner case
	if not candidates or not target:
	    return []
	candidates.sort()
	result = []
	self.dfs(candidates, target, 0, [], result)
	return result
    def dfs(self, candidates, target, sindex, combination, result):
	# base case
	if target == 0:
	    result.append([] + combination)
	    return
	if target < 0:
	    return 
	for i in xrange(sindex, len(candidates)):
	    combination.append(candidates[i])
	    self.dfs(candidates, target-candidates[i], i, combination, result)
	    del combination[-1]

if __name__ == "__main__":
    ans = Solution()
    if ans.combinationSum([2,3,6,7], 7) == [[2,2,3], [7]]:
	print("Passed: Combinationsum implementation.")
    else:
	print("Failed: Combinationsum implementation.")













