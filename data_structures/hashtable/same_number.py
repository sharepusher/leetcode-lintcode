## Reference
# https://www.lintcode.com/problem/same-number/description

## Easy - HashTable - Google

## Description
# Given an array, If the same number exists in the array, 
# and the minimum distance the same number is less than the given value k, output YES, otherwise output NO.
# The length of the given array is n，and n <= 100000.
# The element is x，0 <= x <= 1e9.
# 1 <= k < n

## Example
# Input:  array = [1,2,3,1,5,9,3] and k = 4
# Output: "YES"
# Explanation:
# The distance of 1 whose indexes are  3 and 0 is 3, which meets the requirement and output YES.

# Input:  array = [1,2,3,5,7,1,5,1,3] and k = 4
# Output: "YES"
# Explanation:
# The distance of 1 whose indexes are 0 and 5 is 5, which meets the requirement， and output YES.

## Solution
# 1) there's same numbers in the array; 
# 2) the distance between them < k (counting by index, j -i < k )
# 3) Return directly whenever there's a distance that smaller than k, no matter it's minimal or not! Therefore, no relationship with minmal distance.
# 4) Return "YES" but not True







