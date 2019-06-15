## Reference
# https://www.lintcode.com/problem/double-factorial/description

## Easy - Recursion

## Description
# Given a number n, return the double factorial of the number.
# In mathematics, the product of all the integers from 1 up to some non-negative integer n that have the same parity (odd or even) 
# as n is called the double factorial.
# We guarantee that the result does not exceed long.
#n is a positive integer
## Example 
# Input: n = 5
# Output: 15
# Explanation:
# 5!! = 5 * 3 * 1 = 15
## Input: n = 6
# Output: 48
# Explanation:
# 6!! = 6 * 4 * 2 = 48

## Analysis
# n!! = n * (n-2)!! 
# n!! = 1 if n = 0 or n = 1

## Solution






