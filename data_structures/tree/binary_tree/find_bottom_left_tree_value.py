## Reference
# https://www.lintcode.com/problem/find-bottom-left-tree-value/description
# 513 https://leetcode-cn.com/problems/find-bottom-left-tree-value/

## Medium - BinaryTree/Microsoft

## Description
# Given a binary tree, find the leftmost value in the last row of the tree.
# You may assume the tree (i.e. the given root node) is not NULL

# Example
# Input:{2,1,3}
# Output:1
# Explanation:
#   2
#  /  \
# 1   3

# Input:{1,2,3,4,5,6,#,#,7}
# Output:7
# Explanation:
#          1
#         /  \
#        2    3
#       / \   /
#      4   5 6
#       \
#        7

## Anlaysis
# BFS - only need to record one item. np necessary to record all the items of the row.
# DFS - recodd the max level left item, both left and right should be traversed
# as it's not a full binary tree, right subtree may bigger than the left.

# O(N) time - O(1) space
# BFS is easier to understand than DFS.
# DFS - find the max level and return left most value



