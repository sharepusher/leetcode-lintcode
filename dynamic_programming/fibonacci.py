## Reference
# http://www.lintcode.com/en/problem/fibonacci/

## Tags - Easy
# Mathematics; Recursion; DP

## Description
# Find the Nth number in Fibonacci sequence.
# A Fibonacci sequence is defined as follow:
# 1) The first two numbers are 0 and 1.
# 2) The ith number is the sum of i-1th number and i-2th number.
# The first ten numbers in Fibonacci sequence is:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...
# NOTICE:
# The Nth fibonacci number won't exceed the max value of signed 32bits integer in the test cases.
# Example:
# Given 1, return 0; Given 2, return 1; Given 10, return 34

## Analysis
# 1) according to its definition, recursion can solve it properly.
# 2) DP is also suitable with this kind of issue.  

## Solutions
class Solution(object):
    # recursion - Time Limit Exceeded
    # key: the 1st and 2nd number is 0 and 1.
    # in other words, when n == 1, the ans is 0
    def fibonacci(self, n):
	if n <= 1:
	    return 0
	if n == 2:
	    return 1
	return self.fibonacci(n-1) + self.fibonacci(n-2)
    # DP - O(N)time; O(1)space
    def fibonacci2(self, n):
	if n <= 1:
	    return 0
	if n == 2:
	    return 1
	f1, f2 = 0, 1
	for i in xrange(3, n+1):
	    fn = f1 + f2
	    f1, f2 = f2, fn
	return fn

