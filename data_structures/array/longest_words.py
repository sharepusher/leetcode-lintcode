## Reference
# http://www.lintcode.com/en/problem/longest-words/#

## Tags - Easy
# String; Stack; Enumeration

## Description
# Given a dictionary, find all of the longest words in the dictionary
# Example
# { "like", "love", "yes" } 
# The longest words are ["like", "love"]

## Challenge
# Do it in one pass

## Solutions
class Solution:
    # two pass
    def longestWords1(self, dictionary):
	if not dictionary:
	    return []
	# one pass to calculate the max length
	maxlen = max([len(word) for word in dictionary])
	# one pass to find the words of the maxlen
	return [word for word in dictionary if len(word)== maxlen]
    # one pass
    # stack
    def longestWords2(self, dictionary):
	if not dictionary:
	    return []
	longest = []
	maxlen = 0
	for word in dictionary:
	    if len(word) >= maxlen:
		if len(word) == maxlen:
		    longest.append(word)
		else:
		    longest = [word]
		    maxlen = len(word)
	return longest

if __name__ == "__main__":
    ans = Solution()
    d = ["like", "love", "yes"]
    a = ["like", "love"]
    if ans.longestWords1(d) == a and ans.longestWords2(d) == a:
	print("Passed: longest words.")
    else: 
	print("Failed: longest words.") 

