## Reference
# https://www.lintcode.com/problem/valid-anagram/description

## Easy - String/CrackingTheCodingInterview - Yelp/Uber/Amazon

## Description
# Write a method anagram(s, t) to decide if two strings are anagrams or not.

# Clarification
# What is Anagram?
# Two strings are anagram if they can be the same after change the order of characters.
## Example
# Input: s = "ab", t = "ab"
# Output: true
#
# Input:  s = "abcd", t = "dcba"
# Output: true
#
# Input:  s = "ac", t = "ab"
# Output: false

## Challenge
# O(N)time, O(1)space

## Analysis
# 1. Hash: collections.Counter - O(N)space
# 2. array - O(1) space : counter = [0]*256 (including all ascii symbols)
#   ord(char) to convert the characters to number
#   





