## Reference
# http://www.lintcode.com/en/problem/binary-tree-serialization/#

## Tags - Medium - Uber/Google/Yahoo/Linkedin/Amazon/Facebook/Microsoft/Bloomberg - BFS


## Description
# Design an algorithm and write code to serialize and deserialize a binary tree.
# Writing the tree to a file is called 'serialization' and reading back from the file to
# reconstruct the exact same binary tree is 'deserialization'.
## NOTICE:
# There is no limit of how you deserialize or serialize a binary tree.
## Example
# An example of testdata: BinaryTree{3, 9, 20, #, #, 15, 7}, denote the following structure:
# Input：{3,9,20,#,#,15,7}
# Output：{3,9,20,#,#,15,7}
# Explanation：
# Binary tree {3,9,20,#,#,15,7},  denote the following structure:
# 	  3
# 	 / \
#	9  20
#	  /  \
#	 15   7
# it will be serialized {3,9,20,#,#,15,7}
# 
# Input：{1,2,3}
# Output：{1,2,3}
# Explanation：
# Binary tree {1,2,3},  denote the following structure:
#    1
#   / \
#  2   3
# it will be serialized {1,2,3}
# Our data serialization use BFS traversal. 
# This is just for when you got Wrong Answer and want to debug the input
# You can use other method to do serializaiton and deserialization.

##




