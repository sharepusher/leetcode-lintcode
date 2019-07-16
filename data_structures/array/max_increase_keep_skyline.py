## Reference
# https://www.lintcode.com/problem/max-increase-to-keep-city-skyline/solution

## Easy - 2DArray

## Description
# In a 2D array grid, each value grid[i][j] represents the height of a building located there.
# We are allowed to increase the height of ANY number of buildings, by ANY amount
# The amount can be different fro different buildings.
# Height 0 is considered to be a building as well.

# At the end, the "skyline" when viewed from all four directions of the grid,
# i.e. west, east, north, and south, must be the same as the skyline of the original grid.
# A city's skyline is the outer contour of the rectangles formed by all the buildings 
# when viewed from a distance. See the following examples.

# What is the maximum total sum that the height of the buildings can be increased?
# 1. < grid.length = grid[0].length <= 50.
# 2. All heights grid[i][j] are in the range[0, 100].
# 3. All buildings in grid[i][j] occupy the entire grid cell
# that is, they are a 1x1xgrid[i][j] rectangular prism.

## Example
# Example 1: 
# Input:
#  [ [3,0,8,4],
#    [2,4,5,7],
#    [9,2,6,3],
#    [0,3,1,0] ]
# Output: 35
# Explanation:
#  The skyline viewed from north or south is: [9, 4, 8, 7]
#  The skyline viewed from west or right is: [8, 7, 9, 3]
#  The grid after increasing the height of buildings without affecting skylines is:
#  [ [8,4,8,7],
#    [7,4,7,7],
#    [9,4,8,7],
#    [3,3,3,3] ]
# Example2:
# Input: [[0,0,0],[0,0,0],[0,0,0]]
# Output: 0

## Analysis
# 1) The skyline are the maximum of each row and column
# 2) The increased index should not beyond the min(max_i, max_j)




