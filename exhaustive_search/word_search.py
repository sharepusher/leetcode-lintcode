## Reference
# http://www.lintcode.com/en/problem/word-search/
# 79 https://leetcode.com/problems/word-search/#/description

## Tags - Medium; Yellow
# Backtracking; Facebook

## Description
# Given a 2D board and a word, find if the word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring.
# The same letter cell may not be used more than once.
# Example:
# Given board = [  
#    "ABCE",
#    "SFCS",
#    "ADEE"  ]
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.

## Analysis
# As the direction can go anywhere, therefore, DP can not handle it, use DFS.
# duplicates check needed. as same letter cell may NOT be used more than once.
# How? visited array; or visited hashmap; or mark special character to indicate the visiting
# 1) how to find the first word in the board? traverse the board one by one
# 2) how to dfs? the word can go up/down/left/right. use index to indicate the walk
#    helper function (board, word, visited, x, y, windex)
#    DFS should check index and x,y first, as this is the pre-condition for further validation.
#    if they've already out of index, then the visited and comparasion will be invalid.

## Solutions
class Solution(object):
    # @params: 2D board characters; word string
    # @return: True if the word found
    def exist(self, board, word):
	# corner case
	if not board or not word:
	    return False
	if len(word) == 0:
	    return True
	visited = {}
	for i in xrange(len(board)):
	    for j in xrange(len(board[0])):
		if board[i][j] != word[0]:
		    continue
		if self.dfs(board, word, visited, i, j, 0):
		    return True
	return False
    # dfs search word characters 
    def dfs(self, board, word, visited, x, y, i):
	# base case
	# check word first, as which 
	if  i == len(word):
	    # word find, search should stop
	    return True
	# if the word isn't found yet, check the boundary
	if not (0 <= x <= len(board)-1 and 0 <= y <= len(board[0])-1):
	    return False
	# check duplicates 
	if (x, y) in visited:
	    return False
	if board[x][y] != word[i]:
	    return False
  	# label visited
	visited[(x, y)] = True
	# walk up/down/lef/right to search the word
	up = self.dfs(board, word, visited, x-1, y, i+1)
	down = self.dfs(board, word, visited, x+1, y, i+1)
	left = self.dfs(board, word, visited, x, y-1, i+1)
	right = self.dfs(board, word, visited, x, y+1, i+1)
	if up or down or left or right:
	    return True
	del visited[(x,y)]
	return False	
	    
if __name__ == "__main__":
    board = ["ABCE", "SFCS", "ADEE"]
    word1, word2, word3 = "ABCCED", "SEE", "ABCB"
    # ans1, ans2, ans3 = True, True, False
    ans = Solution()
    if ans.exist(board, word1) and ans.exist(board, word2) and not ans.exist(board, word3):
	print("Passed: word search.")
    else:
	print("Failed: word search.")
