## Reference
# https://www.lintcode.com/problem/single-number/description

## Easy - BitManipulation - Airbnb/Palantir/PalantirTech

## Descripton
# Given 2 * n + 1 numbers, every numbers occurs twice except one, find it.
# n≤100

## Example
# Input：[1,1,2,2,3,4,4]
# Output：3
# Explanation: Only 3 appears once

# Input：[0,0,1]
# Output：1
# Explanation: Only 1 appears once

# Challenge
# One-pass, constant extra space.

## Solution
# 1. Sort and one pass stack
# 2. XOR
# 3. hash count and one pass => 2 pass O(N)space and O(N)time

