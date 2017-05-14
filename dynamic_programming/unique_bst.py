## Reference
# 96https://leetcode.com/problems/unique-binary-search-trees/#/description
# http://www.lintcode.com/en/problem/unique-binary-search-trees/#

## Tags - Medium; Yellow
# BST; DP; Catalan Number.

## Description
# Given n, how many structurally unique BSTs that store values 1...n?
# Example:
# Given n = 3, there are a total of 5 uniqueBST's
# 1           3    3       2      1
#  \         /    /       / \      \
#   3      2     1       1   3      2
#  /      /       \                  \
# 2     1          2                  3

## Analysis
# 1) the number of unique BSTs depends on how many numbers but not values.
#    in other words, (1,2,3) and (5,6,7) have same unique BSTs 1, 2, 3 =>4<= 5, 6, 7;
# 2) the number of unique BSTs of num i, equals to left bst's multiple right bst's

## Solutions
# Time-O(N^2) => arithmetic progression((N^2)/2); space O(N)
class Solution(object):
    def numTrees(self, n):
	if n < 0:
	    return 0
	if n <= 1:
	    return 1
	# init the dp storage
	# we need figure out the counter[n], therefore, totally, n+1 numbers
	# counter[i]: the unique bst's from 0 to i
	counter = [0] * (n+1)
	counter[0], counter[1] = 1, 1
	for i in xrange(2, n+1):
	    # sum up all the counters before i
	    for j in xrange(i):
	        counter[i] += (counter[j]*counter[i-1-j])
	return counter[n]

