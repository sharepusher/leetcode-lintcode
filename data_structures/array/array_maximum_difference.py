## Reference
# https://www.lintcode.com/problem/array-maximum-difference/description

## Easy - Goldman Sachs

## Description
# Given an array a, output the maximum value of a[j] - a[i], where i<j, a[i]<a[j], a[i] is an odd number, and a[j] is an even number

# Example1
# Input: a = [1,2,3,4]
# Output: 3

# Example2
# Input: a = [32,8,54,62,63,99,32,24,36,87]
# Output: 0



## Analysis
# integer: including postive and negative, which can be divided two parts: odd and even.
# what is odd: 2k+1(k!=0);
# what is even: 0 is the special even.
# default return when array is empty or no condition meet the requirement.

# a[i] < a[j], i < j, then a[j]-a[i] > 0. The min difference is 0.


# brute-force
# O(N^2)

