## Reference
# https://www.lintcode.com/problem/longest-substring-without-repeating-characters/

## Medium - HashTable/String/TwoPointer - Adobe/Amazon/Bloomberg/Yelp

## Description
# Given a string, find the length of the longest substring without repeating characters.

## Example
# Input: "abcabcbb"
# Output: 3
# Explanation: The longest substring is "abc".

# Input: "bbbbb"
# Output: 1
# Explanation: The longest substring is "b".

## Challenge
# time complexity O(n)

## Solution
# 1. O(N^2)time; O(N)space => fix the left, and extend the right
# 2. O(N) time; O(N) space => save the time by repeated re-construct the substr from j=i to j= N => visited_unique_substr= set()
# KEY: 1) couting the substr size by len(unique_substr); the visited_substr only contain the valid i-j, remove i whenever a new substr start

##






