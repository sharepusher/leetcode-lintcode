## Reference
# http://www.lintcode.com/en/problem/binary-tree-postorder-traversal/


## Tags - Easy
# Binary Tree; Binary Tree Traversal; Recursion


## Challenge
# Can you do it without recursion


## Description 
# Given a binary tree, return the postorder traversal of its node's values.
 

## Analysis
# input - root of the binary tree;
# output - list of node values in post-order
# kind of DFS; recursion; non-recursion(iteration)
# recursion: Divide and conquer
# when to return: 1) when None; 2) when know left and right node, return left+right+root.val

# Time - O(N), space - O(N)


## Solution
# define the binary tree 
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    # DFS - nonrecursion(iteration): by using customized stack but not system stack
    # the reversed order is easier to figure out,
    # so we can get the normal order first, (NOT pre-order), and then reverse it to the sequence
    # post order required
    # the postorder is left, right, root; so if the proper sequence we are seeking is root, right, left
    # but not the pre-order sequence
    def postorderTraversal4(self, root):
        result = []
        if not root:
            return result
        stack = [root]
        while stack:
            current = stack.pop()
            result.append(current.val)
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        result.reverse()
        return result

    # use nochild and visited to make sure the root value appended to result lastly.
    def postorderTraversal3(self, root):
        result = []
        if not root:
            return result
        # define stack and init
        stack = [root]
        # previously visited node
        prev = None
        while stack:
            current = stack[-1]
            # no child or childvisited is used to indicate that the node should be pop and update result
            # as if the node has child, it won't be visited again before both of its children been visited. 
            nochild = not current.left and not current.right
            # keep the loop can jump out and append the root node value properly
            # if root node will be always visited than its childen, 
            # according to the enqueue sequence, we may visited root twice, at the first time,
            # we enqueue its left and right child, after visited its children, the root will be pop again
            # at this time, we need to know its has been visited or not
            # or we'll continue enqueue and pop endlessly.
            childvisited = prev and (prev in (current.left, current.right))
            if nochild or childvisited:
                # i.e. the node can be updated to the result directly
                result.append(current.val)
                # and the node is visted, then we can pop it
                prev = current
                stack.pop()
            else:
                # has child and not visited
                # pay attention to the order, push right first, and then left
                if current.right:
                    q.append(current.right)
                if current.left:
                    q.append(current.left)
        return result
   
          
               
    # DFS - recursion: divide and conquer
    # return the part of the result, and merge all finally
    def postorderTraversal2(self, root):
        if not root:
            return []
        # get the left part result
        left = self.postorderTraversal(root.left)
        right = self.postorderTraversal(root.right)
        return left+right+[root.val]

    # DFS - recursion: traverse
    # as traverse do not return the result directly, we need the dfshelper to recurse the process
    # and keep the original one
    def postorderTraversal1(self, root):
        result = []
        if not root:
            return result
        # no more extra para
        self.dfshelper(root, result)
        return result
    # the helper will put the values to result
    def dfshelper(self, root, result):
        if not root:
            return
        # as it's post order traversal, so we put the left subtree nodes to results first
        self.dfshelper(root.left, result)
        self.dfshelper(root.right, result)
        # after update left and right in the result, we put the root value to reuslt
        result.append(root.val)

         



