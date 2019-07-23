## Reference
# https://www.lintcode.com/problem/escape-the-ghosts/description

## Medium - Google/Mathematics

## Description
# You are playing a simplified Pacman game. 
# You start at the point (0, 0), and your destination is (target[0], target[1]). 
# There are several ghosts on the map, the i-th ghost starts at (ghosts[i][0], ghosts[i][1]).
# Each turn, you and all ghosts simultaneously may move in one of 4 cardinal directions: north, east, west, or south, 
# going from the previous point to a new point 1 unit of distance away.
# You escape if and only if you can reach the target before any ghost reaches you (for any given moves the ghosts may take).
# If you reach any square (including the target) at the same time as a ghost, it doesn't count as an escape.
# Return true if and only if it is possible to escape, otherwise return false.

# 1. All points have coordinates with absolute value <= 10000.
# 2. The number of ghosts will not exceed 100.

## Example
# Input: ghosts = [[1, 0], [0, 3]], target = [0, 1]
# Output: true
# Explanation: You can directly reach the destination (0, 1) at time 1, while the ghosts located at (1, 0) or (0, 3) have no way to catch up with you.

# Input: ghosts = [[1, 0]], target = [2, 0]
# Output: false
# Explanation: You need to reach the destination (2, 0), but the ghost at (1, 0) lies between you and the destination.

# Input: ghosts = [[2, 0]], target = [1, 0]
# Output: false
# Explanation: The ghost can reach the target at the same time as you.

## Analysis
# The easiest way to catch you is going to the target.
# Therefore, whenever the ghost is near the target than you, he can reach the target and walk around waiting for you.
# Then the problem can be converted to the shortest distance to the target.
# 1) How to find the shorest distance? As you can only walk in four directions.
# Therefore the shortest distance is Manhattan Distance. d = abs(t[x]-s[x])+abs(t[y]-s[y])
# 2) When the Manhattan Distance can replace a DFS search: when only 4 direction allowed; and no details path required only look for the shortest distance.





