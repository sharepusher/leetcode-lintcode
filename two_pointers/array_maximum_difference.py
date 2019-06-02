## Reference
# https://www.lintcode.com/problem/array-maximum-difference/description

## Easy - Goldman

## Description
# Given an array a, output the maximum value of a[j] - a[i], where i<j, a[i]<a[j], 
# a[i] is an odd number, and a[j] is an even number

## Example
# Input: a = [1,2,3,4]
# Output: 3

# Input: a = [32,8,54,62,63,99,32,24,36,87]
# Output: 0

## Solution
# KEY: 1. what is odd and even? they are integer, positive odd, negative odd. 2k+1(k!=0)
#        0 is a special even.
#      2. a[i] < a[j] and i < j ==> the max_diff >0 the min_diff is 0



