## Reference
# http://www.lintcode.com/en/problem/jump-game/#

## Tags - Medium; Frequent
# DP; Greedy

## Description
# Given an array of non-negative integers, you are initially positioned at the first index
# of the array.
# Each element in the array represents your maximum jump length at that position.
# Determin if you are able to reach the last index.
# NOTICE:
# The problem have two method.

## Analysis
# 1) max/min; 2) feasibility/possibility => coordinate DP
# non-negative integers,i.e. >=0; maximum jump length at i, i.e. the jump range(1-ai);
# f[i] - whether can jump to i, which depends on whether there's a j can jump to f[i] 
# f[i] = f[j] and a[j]+j >= i

## Solutions
class Solution(object):
    def canJump(self, nums):
	if not nums:
	    return False
    	N = len(nums)
	# construct the jstat storage
	jstat = [False] * N
	# init the jstat
	jstat[0] = True
	for i in xrange(N):
	    for j in xrange(i):
		jstat[i] = jstat[j] and nums[j]+j >= i
		if jstat[i]:
		    break
	return jstat[-1]


