## Reference
# 17 https://leetcode.com/problems/letter-combinations-of-a-phone-number/#/description
# http://www.lintcode.com/en/problem/letter-combinations-of-a-phone-number/#

## Tags - Medium; Yellow
# Backtracking; String; Uber; Facebook

## Description
# Given a digit string EXCluded 01, return all possible letter combinations that the number could 
# represent. 
# A mapping of digit to letters(just like on the telephone buttons) is given below.
# mapping = {"2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
# NOTICE:
# Although the above answer is in lexicographical order, your answer could be in any order you want.
# Example:
# Given "23"; Return ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

## Analysis
# The letters can be duplicates, but, as it's fixed order, and for each number, the coresponding letters are unique
# and fixed, therefore, we needn't consider the duplicates issue
# 1) the outer index can indicates the index of numbers, and for each dfs, the index increment, in other words,
# we needn't have a for loop to traverse the entire digits, but traverse the letters mapped from digits.
# 2) the inner traverse has no restriction, as the backtracking can lead it to back and forth properly.

## Solution
class Solution(object):
    def letterCombinations(self, digits):
	if not digits:
	    return []
	mapping = {"2": "abc", "3": "def", "4":"ghi", "5":"jkl", "6":"mno", \
	"7": "pqrs", "8": "tuv", "9": "wxyz"}
	result = []
	self.dfs(digits, mapping, 0, [], result)
        return result
    def dfs(self, digits, mapping, dindex, combi, result):
	# base case
	if dindex == len(digits):
	    result.append("".join(combi))
	    return
	word = mapping[digits[dindex]]
	for i in xrange(len(word)):
	    combi.append(word[i])
	    self.dfs(digits, mapping, dindex+1, combi, result)
	    del combi[-1]

if __name__ == "__main__":
    ans = Solution()
    digits = "23"
    if ans.letterCombinations(digits) == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]:
	print("Passed: letter combination of phone number.")
    else:
	print("Failed: letter combination of phone number.")

