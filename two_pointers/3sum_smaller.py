## Reference
# https://www.lintcode.com/problem/3sum-smaller/description

## Medium - Google - TwoPointers/Array

## Description
# Given an array of n integers nums and a target, 
# find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.
## Example:
# Input:  nums = [-2,0,1,3], target = 2
# Output: 2
# Explanation:
# Because there are two triplets which sums are less than 2:
# [-2, 0, 1]
# [-2, 0, 3]

# Input: nums = [-2,0,-1,3], target = 2
# Output: 3
# Explanation:
# Because there are three triplets which sums are less than 2:
# [-2, 0, 1]
# [-2, 0, 3]
# [-2, -1, 3]

## Challenge
# Could you solve it in O(n2) runtime?

## Solution
# 3sum => 2sum


