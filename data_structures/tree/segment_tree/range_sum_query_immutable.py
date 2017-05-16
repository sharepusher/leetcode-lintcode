## Reference
# 303 https://leetcode.com/problems/range-sum-query-immutable/#/description

## Tags - Easy
# DP; SegmentTree

## Description
# Given an integer array nums, find the sum of the elements between indices i and j(i<=j), inclusive.
# Exmaple:
# Given nums = [-2, 0, 3, -5, 2, -1]
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# NOTE: You may assume that the array does NOT change.
# There are many calls to sumRange Function

## Analysis
# The query should be very fast. O(logN) or O(1) is better than O(N).
# DP or segment tree 

## Solutions
# prefix sum
# psum[i]: the sum from beginning to the ith num
# psum[i] = psum[i-1] + num[i]
class NumArray1(object):
    def __init__(self, nums):
	N = len(nums)
	self.psum = [0] * N
	if nums:
	    self.psum[0] = nums[0]
	for i in xrange(1, N):
	    self.psum[i] = self.psum[i-1] + nums[i]
    def sumRange(self, i, j):
        # corner case
	if not self.psum or i > j or j > len(self.psum):
	    return None
        if i > 0:
	    return self.psum[j] - self.psum[i-1]
        else:
	    return self.psum[j]

class SegmentTree(object):
    def __init__(self, start, end, isum):
	self.start, self.end, self.isum = start, end, isum
	self.left, self.right = None, None
    @classmethod
    def build(cls, nums, start, end):
        # corner case
        if not nums or start > end:
	    return None
        # base case
	root = SegmentTree(start, end, nums[start])
	if start == end:
	    return root
        middle = (start + end) // 2
        #print(start, end, middle) 
	root.left = cls.build(nums, start, middle)
	root.right = cls.build(nums, middle+1, end)
	root.isum = root.left.isum + root.right.isum
        return root
    @classmethod
    def query(cls, root, start, end):
	if not root or start > end:
	    return None
	# out of range
	if root.start > end or root.end < start:
	    return None
	if start <= root.start and root.end <= end:
	    return root.isum
	left = cls.query(root.left, start, end)
        right = cls.query(root.right, start, end)
        if left is None and right is None:
	    return None
	if right is None:
	    return left
        if left is None:
	    return right
	# now both left and right are not None, maybe 0
	return left + right
class NumArray2(object):
    def __init__(self, nums):
        N = len(nums)
        start, end = 0, N-1
	self.root = SegmentTree.build(nums, start, end)
    def sumRange(self, i, j):
	if not self.root or i > j:
	    return None
	return SegmentTree.query(self.root, i, j)
    
class NumArray3(object):
    def __init__(self, nums):
        self.nums = nums
    def sumRange(self, i, j):
	if not self.nums or i > j or j >= len(self.nums):
	    return None    
        return sum(self.num[i:j+1])

if __name__ == "__main__":
    nums1 =  []
    nums2 = [-2, 0, 3, -5, 2, -1]
    ans1 = NumArray1(nums1)
    ans2 = NumArray2(nums1)
    ans3 = NumArray1(nums2)
    ans4 = NumArray2(nums2)
    if ans1.sumRange(0, 2) == ans2.sumRange(0,2) and ans3.sumRange(0,2) == ans4.sumRange(0,2) and \
    ans3.sumRange(2,5) == -1 and ans4.sumRange(2, 5) == -1:
        print("Passed: Range Sum Query - Immutable") 
    else:
        print("Failed: Range Sum Query - Immutable") 
	



	    

