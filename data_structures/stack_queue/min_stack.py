## Reference
# 155 https://leetcode.com/problems/min-stack/#/description

## Tags - leetcode Easy; lintcode Medium; RED
# Stack; Google; Uber; Zenefits 

## Description
# Implement a stack with min() function, which will return the smallest number in the stack.
# It should support push, pop and min operation all in O(1) cost.
# In other words, the min stack wanna an extra getMin function on stack.

# push(x) - push element x onto stack.
# pop() - removes the element on top of the stack.
# top() - get the top element
# getMin() - Retrieve the minimum element in the stack.
# Example:
# push(1); pop()   // return 1; push(2); push(3); min()   // return 2
# push(1); min()   // return 1

## Analysis
# As all operation in O(1) cost, we'd better use an extra stack to store the min ones.

## Solution
class MinStack(object):
    def __init__(self):
	self.stack = []
	self.minstack = []
    
    def push(self, x):
	if x is None:
	    return
	self.stack.append(x)
	if x < self.minstack[-1]:
	    self.minstack.append(x)
	else:
	    self.minstack.append(self.minstack[-1])
    def pop(self):
	if not self.stack:
	    return
	self.stack.pop()
	self.minstack.pop()
    def top(self):
	if not self.stack:
	    return None
	return self.stack[-1]
    def getMin(self):
	if not self.stack:
	    return None
	return self.minstack[-1]

if __name__ == "__main__":
    obj = MinStack()
    obj.push(1)
    obj.push(2)
    obj.push(1)
    obj.pop()
    top = obj.top()
    mini = obj.getMin
    if top == 2 and mini == 1:
	print("Passed: Minstack.") 
    else:
	print("Failed: Minstack.") 
