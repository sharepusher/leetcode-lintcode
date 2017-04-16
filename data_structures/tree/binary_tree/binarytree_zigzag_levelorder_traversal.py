## Reference
# http://www.lintcode.com/en/problem/binary-tree-zigzag-level-order-traversal/


## Tags - Medium
# 



## Description
# Given a binary tree, returnthe zigzag level order traversal of its nodes' values.
# i.e. from left to right, then right to left for the next level and alternate between.
# Example:
# Given binary tree {3, 9, 20, #, #, 15, 7}
# Return its zigzag level order traversal as: 
# [ [3]
#  [20, 9]
#  [15, 7]
# ]


## Analysis
# input: root of the binary tree
# output: list of nodes values in zigzag order
# the rule is: even level is from left to right; odd level is from right to left
# the triky solution is to reverse the odd level nodes after collection.
# solution: use a level flag to distinguish the node append order.


## Solution
# definition of tree node
class TreeNode:
    def __init__(val):
        sefl.val = val
        self.left, self.right = None, None

class Solution:
    # one queue BFS = while + deque
    # key: how to convert from right to left 
    # even: from left to right; odd: from right to left
    # 1) normal order, reverse finally
    def zigzagLevelOrder1(self, root):
        if not root:
            return []
 	result = []
	from collections import deque
	q = deque([root])
	while q
	    qlen = len(q)
	    level = []
	    for i in xrange(qlen):
	        curr = q.popleft()
		level.append(curr.val)
		for node in (curr.left, curr.right):
		    if node:
		        q.append(node)
  	    if len(result) % 2 != 0:
		result.append(level.reverse())
            else:
		result.append(level)
	return result

    
