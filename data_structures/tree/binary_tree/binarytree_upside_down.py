## Reference
# https://www.lintcode.com/problem/binary-tree-upside-down/description

## Medium - Linkedin - BinaryTree/DFS

## Description
# Given a binary tree where all the right nodes are either leaf nodes with a sibling or empty
# flip it upside down and turn it into a tree where the original right nodes turned into left leaf nodes.
# Return the new root.

## Example
# Input: {1,2,3,4,5}
# Output: {4,5,2,#,#,3,1}
# Explanation:
# The input is
#    1
#   / \
#  2   3
# / \
#4   5
# and the output is
#   4
#  / \
# 5   2
#    / \
#   3   1 

# Input: {1,2,3,4}
# Output: {4,#,2,3,1}
# Explanation:
# The input is
#    1
#   / \
#  2   3
# /
#4
#and the output is
#   4
#    \
#     2
#    / \
#   3   1

## Solution
# KEY: the new root should be the left leaf node
# And after the upside down, the root.left.left is root.right, and root.left.right is root.





