## Reference
# https://www.lintcode.com/problem/substring-with-at-least-k-distinct-characters/description

## Medium - TwoPointers

## Description
# Given a string S with only lowercase characters.
# Return the number of substrings that contains at least k distinct characters.
# 10 ≤ length(S) ≤ 1,000,000
# 1 ≤ k ≤ 26

## Example
# Input: S = "abcabcabca", k = 4
# Output: 0
# Explanation: There are only three distinct characters in the string.

# Input: S = "abcabcabcabc", k = 3
# Output: 55
# Explanation: Any substring whose length is not smaller than 3 contains a, b, c.
#     For example, there are 10 substrings whose length are 3, "abc", "bca", "cab" ... "abc"
#     There are 9 substrings whose length are 4, "abca", "bcab", "cabc" ... "cabc"
#     ...
#     There is 1 substring whose length is 12, "abcabcabcabc"
#     So the answer is 1 + 2 + ... + 10 = 55.

## Solution
# 1. Brute-force: the total can be counted by N-j
# 2. two-pointers: for and while, the KEY is the counter is N-right+1, and when len(visited)!=k, 
# then the substring is invalid


