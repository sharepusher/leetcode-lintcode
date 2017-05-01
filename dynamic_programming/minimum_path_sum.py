## Reference
# 64 https://leetcode.com/problems/minimum-path-sum/#/description
# http://www.lintcode.com/en/problem/minimum-path-sum/#

## Tags - lintcode Easy; leetcode Medium
# Array; DP

## Description
# Given a mxn grid filled with non-negative numbers, find a path from top left 
# to bottom right which minimizes the sum of all numbers along its path.
# NOTE: You can only move either down or right at any point in time.

## Analysis
# 1) The path is from top left to bottom right, and along the diagonal.
# 2) The min path sum is min(top, and left) + current value
# f[[x][y] = min(f[x-1][y], f[x][y-1]) + g(x,y) 

## Solutions
class Solution(object):
    #DP Top-dwon
    def minPathSum1(self, grid):
	if not grid:
	    return 0
	M, N = len(grid), len(grid[0])
	# construct the dp storage
	psum = [[0 for j in xrange(N)] for i in xrange(M)]
	# init the start point and edges
	psum[0][0] = grid[0][0]
	for i in xrange(1, M):
	    psum[i][0] = psum[i-1] + grid[i][0]
	for j in xrange(1, N):
	    psum[0][j] = psum[0][j-1] + grid[0][j]
	# from 0, 0 to i,j
	for i in xrange(1, M):
	    for j in xrange(1, N):
	        psum[i][j] = min(psum[i-1][j], psum[i][j-1]) + grid[i][j]
	return psum[M-1][N-1]    

    # DP bottom-up
    def minPathSum2(self, grid):
	if not grid:
	    return 0
	M, N = len(grid), len(grid[0])
	# construct dp storage
	psum = [[0 for j in xrange(N)] for i in xrange(M)]
	# init the start point and edges
	psum[M-1][N-1] = grid[M-1][N-1]
	for i in xrange(M-2, -1, -1):
	    psum[i][N-1] = psum[i+1][N-1] + grid[i][N-1]
	for j in xrange(N-2, -1, -1):
	    psum[M-1][j] = psum[M-1][j+1] + grid[M-1][j]
	# calculate x,y to bottom
	for i in xrange(M-2, -1, -1):
	    for j in xrange(N-2, -1, -1):
		psum[i][j] = min(psum[i+1][j], psum[i][j+1]) + grid[i][j]
	return psum[0][0]
	    
    # DFS + memorization
    # helper(self, x,y, grid, visited)
    def minPathSum3(self, grid):
	if not grid:
	    return 0
	# construct the memory
	visited = {}
	return self.helper(0, 0, grid, visited)
    # dfs helper - traverse and return the minpath sum from 0,0
    def helper(self, x, y, grid, visited):
	# reach the boundary - return -1 but not 0 as there's 0 values in the grid
	# at that case, it may retrun 0, we have to distinguish 0 and the dead end.
	# base case
	if x >= len(grid) or y >= len(grid[0]):
	    return -1
	if (x,y) in visited:
	    return visited[(x,y)]
	left = self.helper(x+1, y, grid, visited)
	right = self.helper(x, y+1, grid, visited)
	if left == -1 and right == -1:
	    visited[(x,y)] = grid[x][y]
	elif left == -1:
	    visited[(x,y)] = right + grid[x][y]
	elif right == -1:
	    visited[(x,y)] = left + grid[x][y]
	else:
	    visited[(x,y)] = min(left, right) + grid[x][y]
	return visited[(x,y)]

