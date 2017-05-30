## Reference
# http://www.lintcode.com/en/problem/length-of-last-word/
# 58 https://leetcode.com/problems/length-of-last-word/#/description

## Tags - Easy; Blue
# String

## Description
# Given a string s consits of upper/lower-case alphabets and empty space characters ' '
# return the length of last word in the string.
# if the last word does not exist, return 0.
# A word is defined as a character sequence consist of non-space characters only.
# Example
# Given s = "Hello World", return 5.

## Analysis
# 1) traverse: the last word maybe ending with spaces, therefore, should make sure 
#  the spaces will be omitted
# 2) the split library can help, but with extra space.

## Solutions
# @param {string}
# @return: {int} the length of last word.
class Solution:
    def lengthOfLastWord1(self, s):
	if not s:
	    return 0
	return len(s.strip().split(" ")[-1])
    def lengthOfLastWord2(self, s):
	if not s:
	    return 0
	counter = 0
	N = len(s)
	i = N-1
	while i >= 0:
	    # handle the empty at the end of tail
	    while i >= 0 and s[i] == " ":
		i -= 1
	    # now the tail finished.
	    while i >= 0 and s[i] != " ":
		counter += 1
		i -= 1
	    # now the counter finished.
	    return counter
	return counter

if __name__ == "__main__":
    s = "hello, world"
    length = 5
    ans = Solution()
    if ans.lengthOfLastWord1(s) == length and ans.lengthOfLastWord2(s) == length:
	print("Passed: length of last word.")
    else:
	print("Failed: length of last word.")
