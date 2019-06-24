## Reference
# https://blog.csdn.net/feifeiiong/article/details/76379966
# https://www.lintcode.com/problem/2-keys-keyboard/solution

## Medium - Microsoft/DP

## Description
# Initially on a notepad only one character 'A' is present.
# You can perform two operations on this notepad for each step:
# 1. Copy All: You can copy all the characters present on the notepad(partial copy is not allowed)
# 2. Past: You can paste the characters which are copied last time.
# Given a number n. You have to get EXACTLY n 'A' on the notepad by performing the minimum number of steps permitted.
# Output the minimum number of steps to get n 'A'.
# The n will be in the range [1, 1000].
# 
## Example
# Input: 3
# Output: 3
# Explanation:
# Intitally, we have one character 'A'.
# In step 1, we use Copy All operation.
# In step 2, we use Paste operation to get 'AA'.
# In step 3, we use Paste operation to get 'AAA'.

# Example 2:
# Input: 1
# Output: 0

## Analysis
# 1) EXACTLY N, which means, we cannot copy more than N characters
# 2) when to copy all? j means the numbers on the notepad, i means characters to be copied
# 3) how many times to past: the past times should be k*j=i => k=i/j
# 4) find the minimal past, by which we need j greater
# then the dynamic function is dp[i] = dp[j] + i/j (i%j==0)
# As the max operation for i is i(for i > 2, as you can copy once and past as many as you can), exclude the i== 1

## Solution
#


