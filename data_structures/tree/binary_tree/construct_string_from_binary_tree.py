## Reference
# https://www.lintcode.com/problem/construct-string-from-binary-tree/description

## Easy - Amazon - BinaryTreeTraversal

## Description
# You need to construct a string consits of parenthesis and integers from a binary tree with the preorder traversing way.
# The null node to be represented by empty parenthesis pair "()". 
# And you need to omit all the empty parenthesis pairs that don't affect the one-to-one mapping
# relationship between the string and the original binary tree.

## Example
# Input: Binary tree: [1,2,3,4]
#       1
#     /   \
#    2     3
#   /
#  4
#
# Output: "1(2(4))(3)"

# Explanation: Originallay it needs to be "1(2(4)())(3()())", 
# but you need to omit all the unnecessary empty parenthesis pairs. 
# And it will be "1(2(4))(3)".

# Input: Binary tree: [1,2,3,null,4]
#       1
#     /   \
#    2     3
#     \
#      4
# Output: "1(2()(4))(3)"
# Explanation: Almost the same as the first example, 
# except we can't omit the first parenthesis pair to break the one-to-one mapping relationship between the input and the output.

## Analysis
# KEY: left node parenthesis should always be kept when there's right node available


## Definition of TreeNode
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    # @param t: the root of tree
    # @return: return a string
    def tree2str(self, t):
        pass


