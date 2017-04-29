## Reference
# 88 https://leetcode.com/problems/merge-sorted-array/#/description

## Tags - Array; Two pointers
# Easy

## Description
# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# NOTE: You may assume that nums1 has enough space(size is greater or equal to m+n) to hold additonal 
# elements from nums2.
# The number of elements initialized in nums1 and nums2 are m and n respectively.

## Analysis
# This is somewhat tricky on the solution.
# If we compare from the begainning, then we need insert the comparation result if make it in place.
# The time will be O(N^2)
# As nums1 has enough space, we should compare from the end.
# Then the time is O(M*N)
# So the key of this problem is two pointers with reversed traversal, and append the biggest one by one.

## Solutions
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        if not n:
	    return
	i, j, k = m-1, n-1, m+n-1
	while i >= 0 and j >= 0:
	    if nums1[i] >= nums2[j]:
	        nums1[k] = nums1[i]
		i -= 1
		k -= 1
	    else:
	        nums1[k] = nums2[j]
		j -= 1
		k -= 1
	# now finished the comparison
	while i >= 0:
	    nums1[k] = nums1[i]
	    i -= 1
	    k -= 1
	while j >= 0:
	    nums1[k] = nums2[j]
	    k -= 1
	    j -= 1
        return		

