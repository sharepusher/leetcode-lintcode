## Reference
# http://www.lintcode.com/en/problem/heapify/#

## Tags - Medium
# Lintcode Copyright; Heap

## Description
# Given an integer array, heapify it into a MIN-HEAP array.
# For a heap array A, A[0] is the root of heap, and for each parent A[i], A[i*2+1] is the left child
# and A[i*2+2] is the right child. 
# Example:
# Given [3, 2, 1, 4, 5], return [1, 2, 3, 4, 5] or any legal heap array.

## Clarification
## What is heap?
# Heap is a data structure, which usually have three methods: push, pop and top.
# where "push" add a new element; "pop" delete the minimum/maximum element in the heap;
# "top" return the minimum/maximum element
## What is heapify?
# Convert an unordered integer array into a heap array. If it is min-heap, for each element A[i]
# we will get A[i*2+1] >= A[i] and A[i*2+2]>=A[i] 
## What if there is a lot of solutions?
# Return any of them.

## Challenge
# O(N) time complexity

## Analysis
# 1) min-heap array
# 2) sift up or sift down

## Solutions
class Solution:
    # @param: A - given an integer array
    # @return: None, as it's in-place heapify

    # Two types heapify: min-heap; max-heap

    def heapify1(self, A):
	import heapq
        # transform list into a heap, in-place, in linear time.
	heapq.heapify(A)
	return

    def heapify2(self, A):
	if not A:
	    return
	for i in xrange(len(A)):
	    self.siftup(A, i)
	return

    # a heap array, root is i, then left child = 2*i+1; right child = 2*i+2
    # therefore, the parent i = (child-1)//2
    # child_index starts from 0, and compare with its parent, 	    
    def siftup(self, A, child_index):
        # when child index is 0, then it's the root
        # which do NOT have parent.
	while child_index != 0:
	    parent_index = (child_index-1) // 2
            if A[child_index] > A[parent_index]:
		break
	    # now child <= parent
	    # exchange it
	    A[child_index], A[parent_index] = A[parent_index], A[child_index]
	    # After corrected the child parent values
	    # the new parent also should meet the requirement, 
	    # that's why there's a while loop
	    # and we need update the child index to the new parent index, 
	    # then it will sift up as its function name until reaching the root. 
	    child_index = parent_index
	
    def heapify3(self, A):
	if not A:
	    return
	N = len(A)
	parent_index = N//2
        for i in xrange(N//2, -1, -1):
	    self.siftdown(A, i)
    # Start from middle(N//2), compare it with its children.
    # when we know parent index i, the left child index is (2*i+1), the right child is (2*i+2)
    def siftdown(self, A, parent_index):
        N = len(A)
	# parent can not equal to N, as which doesnot have children anymore
	while parent_index < N:
            # parent 
	    smallest = parent_index
            # left candidate
	    if 2*parent_index+1 < N and A[2*parent_index+1] < A[parent_index]:
		smallest = 2*parent_index+1
	    # right candidate
	    if 2*parent_index+2 < N and A[2*parent_index+2] < A[smallest]:
		smallest = 2*parent_index+2
	    if smallest == parent_index:
		break
	    A[parent_index], A[smallest] = A[smallest], A[parent_index]
	    parent_index = smallest
	    
if __name__ == "__main__":
    A, B, C = [3, 2, 1, 4, 5], [3, 2, 1, 4, 5], [3, 2, 1, 4, 5]
    ans = Solution()
    ans.heapify1(A) 
    ans.heapify2(B)
    ans.heapify3(C)
    print(A, B, C)
    if A == [1, 2, 3, 4, 5] and B == [1, 2, 3, 4, 5] and C==[1, 2, 3, 4, 5]:
	print("Passed: heapify")
    else:
	print("Failed: heapify")

	
