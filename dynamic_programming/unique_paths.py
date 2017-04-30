## Reference
# 62 https://leetcode.com/problems/unique-paths/#/description
# http://www.lintcode.com/en/problem/unique-paths/#

## Tags - lintcode Easy/leetcode Medium
#  DP

## Description
# A robot is located at the top-left corner of mxn grid(marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time. The robot is trying to 
# reach the bottom-right corner of the grid(marked 'Finish' in the diagram below).
# How many possible unique paths are there?

## Analysis
# 1) 2D matrix, MXN grid, M may != N; 2) two directions to move; 
# 3) top-left to bottom-right
# 4) sum of possible unique paths
# When to use DP? max/min/possiblility/feasibility/how many
# When not use DP? the exact paths
# Top-down; bottom-up; DFS+memorization
# stat: f(x,y) the unique path from top to x,y
# function: f(x, y) = f(x,y-1) + f(x-1, y)
# init: f(0,0), f(0,i), f(i, 0)
# ans: f(m-1,n-1)
## 

## Solutions
class Solutions(object):
    # top down
    def uniquePaths1(self, m, n):
	# corner case, when the grid is empty, then 0 paths
	if m < 0 or n < 0:
	    return 0
	if m == 1 or n == 1:
	    return 1
	# construct the dp 2d grid
	f = [[1 for j in xrange(n)] for i in xrange(m)]	
	# as f has been inited properly, then we needn't init edges here.
	for i in xrange(1, m):
	    for j in xrange(1, n):
		f[i][j] = f[i-1][j] + f[i][j-1]
	return f[m-1][n-1]

    # bottom-up
    def uniquePaths2(self, m, n):
	if m < 0 or n < 0:
	    return 0
	if m == 1 or n == 1:
	    return 1
	f = [[1 for j in xrange(n)] for i in xrange(m)]
	for i in xrange(m-2, -1, -1):
	    for j in xrange(n-2, -1, -1):
		f[i][j] = f[i+1][j] + f[i][j+1]
	return f[0][0]

    # DFS + memorization
    def uniquePaths3(self, m, n):	
	if m < 1 or n < 1:
	    return 0
	if m == 1 or n == 1:
	    return 1
	visited = {}
	return self.helper(0, 0, m, n, visited)
    def helper(self, x, y, m, n, visited):
	if x >= m or y >= n:
	    return 0
	if (x,y) in visited:
	    return visited[(x,y)]
	left = self.helper(x+1, y, m, n, visited)
	right = self.helper(x, y+1, m, n, visited)
	if left and right:
	    visited[(x,y)] = left + right
	else:
	    # the DFS will go to the bottom and then go back,
	    # therefore, in some extent, dfs is a bottom-up solution
	    # when there's no left right, we know it's bottom, return 1
	    # when there's left or right, then we can say, there's only one 
	    # way to the target.
	    visited[(x,y)] = 1
	return visited[(x,y)]

    def uniquePaths4(self, m, n):
	if m < 1 or n < 1:
	    return 0
	if m == 1 or n == 1:
	    return 1
	visited = {}
	return self.dfs(m, n, visited)
    def dfs(self, m, n, visited):
        ## it won't reach m < 1 or n < 1 
	## as we've filtered that, and return when m == 1 or n==1
	#if m < 1 or n < 1:
	#    return 0
	if m == 1 or n == 1:
	    return 1
	if (m, n) in visited:
	    return visited[(m,n)]
	left = self.dfs(m-1, n, visited)
	right = self.dfs(m, n-1, visited)
	visited[(x,y)] = left + right
	return left + right 


