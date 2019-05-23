## Reference
# https://www.lintcode.com/problem/fruit-into-baskets/solution

## Medium - TwoPointers - Google

## Description
# In a row of trees, the i-th tree produces fruit with type tree[i].
# You start at any tree of your choice, then repeatedly perform the following steps:
# 1.Add one piece of fruit from this tree to your baskets. If you cannot, stop.
# 2.Move to the next tree to the right of the current tree. If there is no tree to the right, stop.
# Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, 
# then step 2, then back to step 1, then step 2, and so on until you stop.
# You have two baskets, and each basket can carry any quantity of fruit, 
# but you want each basket to only carry one type of fruit each.
# What is the total amount of fruit you can collect with this procedure?
# 1 <= tree.length <= 40000
# 0 <= tree[i] < tree.length

## Example
# Input: [1,2,1]
# Output: 3
# Explanation: We can collect [1,2,1].

# Input: [1,2,3,2,2]
# Output: 4
# Explanation: We can collect [2,3,2,2].
# If we started at the first tree, we would only collect [1, 2].

## Solution
# 1) tree[i] is the tree type
# 2) 2 bucket, maximum 2 types of trees can collect.
# 3) longest subarray with at most 2 types of trees




