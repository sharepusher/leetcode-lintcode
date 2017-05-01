## Reference
# http://www.lintcode.com/en/problem/jump-game-ii/

## Tags - Medium
# Greedy; Array

## Description
# Given an array of non-negative integers, you are initially positioned at the first
# index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.
# Example:
# Given array A=[2,3,1,1,4]
# The minimum number of jumps to reach the last index is 2.
# Jump 1 step from 0 to 1, then 3 steps to the last index.

## Analysis
# 1) non-negative integers, i.e. >= 0
# 2) f[i] = min(f[j]+1, f[i])
# 3) at problem1, we'll break we we found it works, but in this problem
#    we have to compare all the works jumps, and compare it and select the min one.
# 4) as we are looking for min, therefore, we need init them as sys.maxint to convenient comparation.

## Solutions
import sys
class Solution(object):
    def jump(self, A):
	if not A:
	    return None
	N = len(A)
    	# construct the dp storage
	jmin = [sys.maxint] * N
	# init the start point
	# the start point needn't pay any effort to reach itself.
	jmin[0] = 0
	for i in xrange(N):
	    for j in xrange(i):
		if A[j] + j >= i:
		    jmin[i] = min(jmin[i], jmin[j]+1)
	return jmin[-1]
		
