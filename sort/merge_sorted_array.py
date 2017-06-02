## Reference
# http://www.lintcode.com/en/problem/merge-sorted-array/#
# 88 https://leetcode.com/problems/merge-sorted-array/#/description

## Tags - Easy; RED
# Sorted Array; Two pointers; Facebook

## Description
# Given two sorted integer arrays A and B, merge B into A as one sorted array.
# Notice: 
# You may assume that A has enough space (size that is greater or equal to m+n) to hold 
# additional elements from B. The number of elements initialized in A and B are m and n respectively.
# Example:
# A = [1, 2, 3, empty, empty], B = [4, 5]
# After merge, A will be filled as [1, 2, 3, 4, 5]

## Analysis
# in-place merge; A has enough space
# As they've sorted, we can merge it reversely

## Solution
class Solution:
    def mergeSortedArray(self, A, m, B, n):
	if not A:
	    A = B
	    return
	if not B:
	    return
	i, j, k = m-1, n-1, (m+n)-1
	while i >= 0 and j >= 0:
	    if A[i] > B[j]:
		A[k] = A[i]
		i -= 1
	    else:
		A[k] = B[j]
		j -= 1
	    k -= 1
	while i >= 0:
	    return
	while j >= 0:
	    A[k] = B[j]
	    k -= 1
	    j -= 1
	return

if __name__ == "__main__":
    A = [1, 2, 3, None, None]
    B = [4, 5]
    An = [1, 2, 3, 4, 5]
    ans = Solution()
    ans.mergeSortedArray(A, 3, B, 2)
    if A == An:
	print("Passed: merge sorted array.")
    else:
        print("Failed: merge sorted array")
