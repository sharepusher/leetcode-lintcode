## Reference
# https://www.lintcode.com/problem/partition-array-ii/description

## Medium - array

## Description
# Partition an unsorted integer array into three parts:
# 1) The front part < low
# 2) The middle part >= low & <= high
# 3) The tail part > high
# Return any of the possible solutions.
# low <= high in all testcases.

## Challenge
# Do it in place.
# Do it in one pass (one loop).

## Example
# Input:
# [4,3,4,1,2,3,1,2]
# 2
# 3
# Output:
# [1,1,2,3,2,3,4,4]
# Explanation:
# [1,1,2,2,3,3,4,4] is also a correct answer, but [1,2,1,2,3,3,4,4] is not

# Input:
# [3,2,1]
# 2
# 3
# Output:
# [1,2,3]

## Solution
# 1) traverse and restore
# 2) partiton twice
# 2)




