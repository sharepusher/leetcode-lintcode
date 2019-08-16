## Reference
# http://www.lintcode.com/en/problem/implement-trie/
# 208 https://leetcode.com/problems/implement-trie-prefix-tree/#/description

## Tags - Medium; Blue
# Trie; Facebook; Uber; Google

## Description
# Implement a trie with insert, search, and startsWith methods.
# NOTE:
# You may assume that all inputs are consist of lowercase letter a-z
# Example:
# insert("lintcode")
# search("code")
# >>> false
# startsWith("lint")
# >>> true
# startsWith("linterror")
# >>> false
# insert("linterror")
# search("lintcode)
# >>> true
# startsWith("linterror")
# >>> true

## Analysis
# Trie is a 26 tree.
# There are two ways to implement trie: hashmap or arraylist
# arraylist spends more space, as which has to pre-allocate
# 1) trie node definition
#   Each node has a word label to indicates whether the word traverse finished.
#   and there's should be a 26bits list or a hashmap to store the reference to other trie nodes
# 2) trie build: trie is not like the segment tree, there's no need to build the tree, but just insert
#    as trie should be a kind of ds that change oftenly.
#    while segment tree is based on a list, that's why it should be build first.
#    Trie build process is performed during insertion.
# 3) trie query  

## Solutions

# Trie 

# implement trie with hash
class TrieNode(object):
    def __init__(self):
        self.children = {} # each children contains TrieNode - "w": TrieNode()
	self.is_word = False
        self.num = 0

class Trie(object):
    def __init__(self):
	"""Initialize the data structure.
        """
        self.root = TrieNode()
    # @return: None
    # build trie tree
    def insert(self, word):
        # corner case
        if not word:
	    return
        walker = self.root
        for letter in word:
	    if letter not in walker.children:
		walker.children[letter] = TrieNode()
            walker = walker.children[letter]
        current.is_word = True
        return

    # @return: True if find the word
    def search(self, words):
	# corner case
	if not word:
	    return False
        if not self.root:
	    return False
	current = self.root
        for letter in word:
	    if letter not in current.children:
		 return False
            current = current.children[letter]
	return current.is_word

    def startswith(self, word):
        if not word or not self.root:
	    return False
	current = self.root
	for letter in word:
	    if letter not in current.children:
		return False
	    current = current.children[letter]
	return True

