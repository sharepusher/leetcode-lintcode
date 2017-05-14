## Reference
# http://www.lintcode.com/en/problem/combinations/#
# 77 https://leetcode.com/problems/combinations/#/description

## Tags - Medium; Blue
# Array; Backtracking

## Description
# Given two integers n and k, return all possible combinations of k numbers out of 1 ...n.
# For example, If n == 4 and k == 2, a solution is:
# [
#  [2,4],
#  [3,4],
#  [2,3],
#  [1,2],
#  [1,3],
#  [1,4],
# ]

## Analysis
# 1) corner case: n >= 1; k >= 1; n >= k; 
# 2) as the number is 1...to...n, therefore, no duplicates should be taking consideration.
# 3) almost the same as the permutation

## Solutions
class Solution(object):
    def combine(self, n, k):
	if n <= 0 or k <= 0 or n < k:
	    return []
	result = []
	self.dfs(n, k, 1, [], result)
	return result
    # collect the combination from start index, and merge them to result
    def dfs(self, n, k, sindex, combination, result):
	# base case
	if k == 0:
	    result.append([]+combination)
	    return 
	# n+1 to handle n==k
	for i in xrange(sindex, n+1):
	    combination.append(i)
	    self.dfs(n, k-1, i+1, combination, result)
	    del combination[-1]
if __name__ == "__main__":
    ans = Solution()
    n1, k1 = 1, 1
    n2, k2 = 4, 2
    if ans.combine(n1, k1) == [[1]] and ans.combine(n2, k2).sort() == [[2,4],[3,4],[2,3],[1,2],[1,3],[1,4]].sort():
	print("Passed: Combination implementation.")
    else:
	print("Failed: Combination implementation.")




