## Reference
# 131 https://leetcode.com/problems/palindrome-partitioning/#/description
# http://www.lintcode.com/en/problem/palindrome-partitioning/#

## Tags - Medium; Blue
# Backtracking; DFS 

## Description
# Given a string s, partition s such that every substring of the partition is a palindrome.
# Return all possible palindrome partitioning of s.
# Example:
# Given s = "aab", return:
# [
#  ["aa","b"],
#  ["a","a","b"]
# ]

## Analysis
# 1) all possible palindrome partitions => DFS
# 2) string immutable
# 3) O(2^N) time; O(N) space

## Solution
class Solution(object):
    # @params: string
    # @return: True if the string is palindrome; otherwise False
    # Two pointer - O(N) time; O(1) space
    def isPalindrome(self, s):
        if not s:
	    return True
	N = len(s)
	start, end = 0, N-1
	while start < end:
	    if s[start] != s[end]:
		return False
	    start += 1
	    end -= 1
	return True
    # pythonic
    # O(N) time; O(N) space
    def isPalindrome1(self, s):
	if not s:
	    return True
	return s == s[::-1]
    # @params: string
    # @return: list of palindrome partitions
    def partition(self, s):
        if not s:
	    return []
	result = []
	self.dfs(s, 0, [], result)
	return result
    # the dfs helper will help collect the partitoned palindrome
    # and merge them to result properly
    def dfs(self, s, sindex, palindrome, result):
	# base case
        # NOTE: we can NOT use the palindrome length here
        # As the len of palindrome is the partition numbers
        # but NOT the end of the traverse
	if sindex == len(s):
	    result.append([]+palindrome)
	    return
	for i in xrange(sindex, len(s)):
	    if not self.isPalindrome(s[sindex:i+1]):
	        continue
            # put the palindrome partition to list
	    palindrome.append(s[sindex:i+1])
	    self.dfs(s, i+1, palindrome, result)
	    #palindrome.pop()
	    del palindrome[-1]

if __name__ == "__main__":
    s1, s2 = "aab", ""
    ans = Solution()
    if ans.partition(s1) == [["a", "a", "b"], ["aa", "b"]] and ans.partition(s2) == []:
        print("Passed: Palindrome Partition.")
    else:
	print("Failed: Palindrome Partition.")
