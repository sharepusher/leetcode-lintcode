## Reference
# 212 https://leetcode.com/problems/word-search-ii/#/description
# http://www.lintcode.com/en/problem/word-search-ii/

## Tags - Hard
# Backtracking, Trie; Airbnb

## Description
# Given a matrix of lower alphabets and a dictionary.
# Find all words in the dictionary that can be found in the matrix.
# A word can start from any position in the matrix and go left/right/up/down to the 
# The same letter cell may not be used more than once in a word.
# For example:
# Given words = ["oath","pea","eat","rain"] and
# board = 
# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# Return ["eat", "oath"]

## Analysis
# We can use backtracking directly just like the word search 1 problem.
# Why use Trie? more efficiency than W * (M^2*N^2)
# NOTE: the board may produce duplicates, therefore, we need avoid duplicates in the result. 
# 1) build trie tree, including word when is_word.
# 2) looking for the leading word by for for to traverse the character matrix 
# 3) dfs(matrix, x, y, trie_root, result)
# 4) label visited? As the same leeter can NOT be used more than once
#    in  a word, we need use a hash to record visited(matrix[x,y])
#    in other words, which is only works in the word search process, not work in other word.

## Solution

# build Trie Tree
class Trie(object):
    def __init__(self):
        self.children = {}
	#self.is_word = False
	self.word = ""
    # build Trie by word
    # NO need to return trie root, as we've know it before the insert operation
    @staticmethod    
    def insert(root, word):
        if not root:
	    return 
        current = root
	for letter in word:
	    if letter not in current.children:
		current.children[letter] = Trie()
	    current = current.children[letter]
        #current.is_word = True
	current.word = word
        return	
    # @return: true or false
    @staticmethod
    def search(root, word):
	if not root or not word:
	    return False
        current = root
	for letter in word:
	    if not current or letter not in current.children:
		return False
	    # now letter in children
	    current = current.children[letter]
        return current.word != ""

class Solution(object):
    def wordSearch2(self, board, words):
        # corner case
	if not board or not words:
	    return []
        # build trie
        root = Trie()
	# insert words
	for word in words:
	    Trie.insert(root, word)
	# traverse the board
        result = []
        for i in xrange(len(board)):
	    for j in xrange(len(board[0])):
		if board[i][j] not in root.children:
		    continue
		# dfs search the word in trie
		self.dfs(board, root, i, j, {}, result)
	return result
    def dfs(self, board, root, x, y, visited, result):
        if not root:
	    return
        # NOTE: make sure no duplicate word in result !!!!
	if root.word and root.word not in result:
	    result.append(root.word)
	    return
	# check boards
	if not (0 <= x < len(board)) or not (0 <= y < len(board[0])) or (x, y) in visited:
	    return  
	if board[x][y] not in root.children:
	    return
	visited[(x, y)] = True
        root = root.children[board[x][y]]
	self.dfs(board, root, x+1, y, visited, result)
	self.dfs(board, root, x-1, y, visited, result)
	self.dfs(board, root, x, y+1, visited, result)
	self.dfs(board, root, x, y-1, visited, result)
        del visited[(x, y)]

if __name__ == "__main__":
    board = ["doaf", "agai", "dcan"]
    words = ["dog", "dad", "dgdg", "can", "again"]
    result = ["dog", "dad", "can", "again"]
    ans = Solution()
    if result.sort() == ans.wordSearch2(board, words).sort():
	print("Passed: word search 2.")
    else:
	print("Failed: word search 2.")
	


