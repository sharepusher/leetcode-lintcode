## Reference
# https://www.lintcode.com/problem/daily-temperatures/description

## Medium - stack/Mo'notonous stack - Google


## Description
# Given a list of daily temperatures, produce a list that, for each day in the input,
# tells you how many days you would have to wait until a warmer temperature.
# If there is no future day for which this is possible, put 0 instead.
# For example, given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# your output should be [1,1,4,2,1,1,0,0]

# the length of temperatures will be in the range[1, 30000].
# Each temperature will be an integer in the range[30, 100]

## Example
# Input:  temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# Output:  [1, 1, 4, 2, 1, 1, 0, 0]
# Explanation:
# Just find the first day after it which has higher temperatures than it.
# Input: temperatures = [50, 40, 39, 30]
# Output:  [0,0,0,0]

## Analysis
# 1. it's obviously that O(N^2) isn't good enough
# 2. Monotonous stack can help find the 1st increase item, and the distance can be calculated by index






