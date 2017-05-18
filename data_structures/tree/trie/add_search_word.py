## Reference
# http://www.lintcode.com/en/problem/add-and-search-word/#
# 211 https://leetcode.com/problems/add-and-search-word-data-structure-design/

## Tags - Medium
# Backtraking; Trie; Design

## Description 
# Design a data structure that supports the following two operations:
# addWord(word) and search(word). search(word) can search a literal word or a regular 
# expression string containing only letters "a-z" or "."
# A "." means it can represent any one letter.
# NOTICE: 
# You may assume that all words are consist of lowercase letters a-z.
# Example:
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad")  // return false
# search("bad")  // return true
# search(".ad")  // return true
# search("b..")  // return true

## Analysis
# The word add can be implemented by trie
# 1) The normal search can also use trie, but the regular expression have to sue the DFS to traverse all the childrens.
# Trie do NOT have a build process like segment tree, it can NOT build at one time. 
# Therefore, the general build is just create the root node for latter add/search operation
# 2) The word search should pay attention to the word length, when the word finished, the label should be True 

## Solutions
# definition of Trie Node
# implement trie with hashtable
class TrieNode(object):
    def __init__(self):
	self.children = {}
        self.is_word = False
	self.nums = 0 # indicate how many words are sharing this character.
class WordDictionary(object):
    # init trie node
    def __init__(self):
	self.root = TrieNode()	
    # @return: None
    def addWord(self, word):
	# corner case
	if not word:
	    return
	current = self.root
	# traverse the letter and update trie tree
	for letter in word:
	    if letter not in current.children:
		current.children[letter] = TrieNode()
	    current = current.children[letter]
	current.is_word = True
    # @params: word to be searched
    # @return: True if found
    def search(self, word):
        # corner case
	if not word:
	    return False
	# how to search
	# 1) according to the trie root, we search normal characters	
	# 2) when "." appears, dfs search all the childrens.
	# as the "." may be appears in the middle or at the beginning, therefore, 
	# we need a helper function to handle all the search process
	# which will return True or false properly.
        current = self.root
	return self.dfs(current, word, 0)
    # search word in trie by dfs, index indicates the start of the word
    # @return True if the word found
    def dfs(self, current, word, windex):
	# base case
        if windex == len(word):
	    return current.is_word
	for i in xrange(windex, len(word)):
	    if not current:
		return False
	    if word[i] in current.children:
		current = current.children[word[i]]
		continue
	    if word[i] not in current.children:
		if word[i] != ".":
		    return False
		# we need do the dfs for "."
	 	for child in current.children:
		    # child is key ! BUT NOT node value
		    # Therefore, it should be current.children[child]
		    if self.dfs(current.children[child], word, i+1):
		        return True
		return False
	return current.is_word

if __name__ == "__main__":
    ans = WordDictionary()
    for word in ("bad", "dad", "mad"):
        ans.addWord(word)
    result = []
    for word in ("pad", "bad", ".ad", "b..", "."):
	result.append(ans.search(word))
    if result == [False, True, True, True, False]:
	print("Passed: Add and Search Word.")
    else:
	print("Failed: Add and Search Word.")
	
 
