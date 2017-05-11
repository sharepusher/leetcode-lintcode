## Reference
# 409 https://leetcode.com/problems/longest-palindrome/#/description
# http://www.lintcode.com/en/problem/longest-palindrome/#

## Tags - Easy;
# HashTable; Amazon

## Description
# Given a string which consists of lowercase or uppercase letters, find the length of the longest
# palindromes that can be built with those letters.
# NOTE:  This is case sensitive.
# Example: 'dbaccccd'; output 7.

## Analysis
# DP? as palindorme length depends on all the previous items. So we cannot make it by DP
# sort? as it's string, so sorted(s) may sort and convert it to list, but still cost O(N) space
# So hash is the a better solution.
# The length depends on the duplicates chars in s, therefore, we have to
# collect and counts the occurence of characters
# And add one single one if necessary.

## Solutions
class Solution(object):
    def longestPalindrome(self, s):
	if not s:
	    return 0
	chars = {}
	longest = 0
	single = 0
	# the index is not necessary, so we needn't check that
	for key in s:
	    if key in chars:
		chars[key] += 1
	    else:
		chars[key] = 1
	# count the longest
	for key in chars:
	    if chars[key] % 2 == 0:
		longest += chars[key]
	    else:
		longest += (chars[key]-1)
		single = 1
	return longest + single

if __name__ == "__main__":
    ans = Solution()
    s = "abccccdd"
    if 7 == ans.longestPalindrome(s):
	print("Passed: longest palindrome.")
    else:
	print("Failed: longset palindrome.")
    
	    
	
