## Reference
# https://www.lintcode.com/problem/permutation-in-string/description

## Medium - Microsoft/Hash/TwoPointers

## Description
# Given two string s1 and s2, write a function to return true if s2 contains the permutation of s1.
# In other words, one of the first string's permutations is the substring of the second string.
# The input string s only contains lower case letters.
# The length of both given strings is in range[1, 10000]
# Example
# Input: s1='ab', s2='eidbaooo'
# Output: True
# Explanation: s2 contains one permutation of s1('ba')
# Input: s1='ab', s2='eidaooo'
# Output: False

## Analysis
# 1. find all the permutation of s1 and check whether one of them in s2
# 2. traverse s2, find whether character in s1, if so, check len(s2) in s1
# 3. sliding window and check whether the substring is permutation of s1

# How to check whether a substring is a permutaiton of string
# 1. permutaiton converstion
# 2. collections.Counter()
# 3. traverse and check whether all the characters are in the string set




