## Reference
# 47 https://leetcode.com/problems/permutations-ii/#/description
# http://www.lintcode.com/en/problem/permutations-ii/#

## Tags - Medium; Blue
# Backtracking(DFS); Linkedin;

## Description
# Given a list of numbers with duplicate number in it. Find all unique permutations.
# Exaple:
# For numbers [1, 2, 2], the unique permutations are:
# [
#   [1,2,2],
#   [2,1,2],
#   [2,2,1]
# ]

## Challenge
# Using recursion to do it is acceptable. Non-recursion would be great.

## Analysis
# All the exact solution => DFS: key is how to avoid the duplicates
# We can NOT handle duplicates based on index or values as what we did on subset
# Therefore, we need extra "visited" storage to avoid duplicates.  
# 
# non-recursion solution for permutation: lexicographic order(4 steps).
# sort first 1) find the largest k that a[k] < a[k+1] in reverse order.
# 2) find the largest j(j < k) such that a[j] < a[k]
# 3) reverse a[k], a[j]
# 4) reverse k+1 to N-1 

## Solutions
class Solution:
    # @params: list of numbers
    # @return: list of unique permutations
    def permuteUnique1(self, nums):
        # corner case
	if not nums:
	    return [nums]
	result = []
        visited = [False] * len(nums)
        # 1) does permutation need index?
	# NO! we need visited array to avoid duplicates but not index
        # as we have to traverse all the list each time.
	# 2) sort or not?
        # Yes! we have to Sort first to simplify the duplicates check
        nums.sort() 
        self.dfshelper(nums, visited, [], result)
	return result
    def dfshelper(self, nums, visited, permutation, result):
        # base case
        if len(permutation) == len(nums):
	    result.append([]+permutation)
	    return 
	for i in xrange(len(nums)):
            # avoid duplicates during constructing a permutation
            if visited[i]:
		continue
	    # avoid create another new duplicate permutation
            # This condition is used to avoid the duplicates permutation in the
            # outer loop
            # why "not visited[i-1]", as it's won't be False unless the new permutation is creating
	    # the visited will be False after a permutation created, at this time, a new one will be started
            # if the new starter is the same as last one, then we needn't start it, as it's duplicated
	    if i != 0 and not visited[i-1] and nums[i] == nums[i-1]:
		continue
	    permutation.append(nums[i])
            visited[i] = True
	    self.dfshelper(nums, visited, permutation, result)
	    visited[i] = False
	    permutation.pop()

    def permuteUnique2(self, nums):
	if not nums:
	    return [nums]
        result = []
	nums.sort()
	N = len(nums)
	while True:
            # merge current permutation
	    result.append([] + nums)
	    # 1) find the largest index k such that a[k] < a[k+1]
            # if no such index, there's no next permutation
	    k, j = 0, 0
	    for k in xrange(N-2, -1, -1):
		if nums[k] < nums[k+1]:
		    break
		if k == 0:
		    return result
	    # 2) find the largest j (j > k) such that a[j] > a[k]
	    for j in xrange(N-1, k, -1):
		if nums[k] < nums[j]:
		    break
	    # 3) swap k, j
	    nums[k], nums[j] = nums[j], nums[k]
	    # 4) reverse k+1->n
	    nums[k+1:] = nums[N-1:k:-1]
        return result

	         
if __name__ == "__main__":
    nums = [1,2, 2]
    ans = Solution()
    if ans.permuteUnique1(nums) == [[1,2,2],[2,1,2],[2,2,1]] and ans.permuteUnique2(nums) == [[1,2,2],[2,1,2],[2,2,1]]:
	print("Passed: Unique Perumutations")
    else:
	print("Failed: Unique Perumutations")
	
