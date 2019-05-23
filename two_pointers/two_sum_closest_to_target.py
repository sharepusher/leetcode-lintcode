## Reference
# https://www.lintcode.com/problem/two-sum-closest-to-target/description

## Medium - Sort/TwoPointer

## Description
# Given an array nums of n integers, find two integers in nums such that the sum is closest to a given number, target.
# Return the absolute value of difference between the sum of the two integers and the target.

## Example
# Input:  nums = [-1, 2, 1, -4] and target = 4
# Output: 1
# Explanation:
# The minimum difference is 1. (4 - (2 + 1) = 1).

# Input:  nums = [-1, -1, -1, -4] and target = 4
# Output: 6
# Explanation:
# The minimum difference is 6. (4 - (- 1 - 1) = 6).

## Challenge
# Do it in O(nlogn) time complexity.

## Solution
# KEY: count all the diff and compare the diff during the process, return finally.




