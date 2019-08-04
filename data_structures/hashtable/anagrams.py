## Reference
# https://www.lintcode.com/problem/anagrams/description

## Medium - String/Hash - Facebook/Uber

## Description
# Given an array of strings, return all groups of strings that are anagrams.
# All inputs will be in lower-case
## Example
# Input:["lint", "intl", "inlt", "code"]
# Output:["lint", "inlt", "intl"]
#
# Input:["ab", "ba", "cd", "dc", "e"]
# Output: ["ab", "ba", "cd", "dc"]

## Challenge
# What is Anagram?
# Two strings are anagram if they can be the same after change the order of characters.

## Analysis
# 1. Sorted - can be applied to string directly: sorted(string_items)
# 2. How to prove anagram? 
#    character set is not enough, word level hash is necessary; 
#    sort string and compare => hash based on sorted word
#






