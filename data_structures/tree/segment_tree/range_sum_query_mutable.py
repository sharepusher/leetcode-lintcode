## Reference
# 307 https://leetcode.com/problems/range-sum-query-mutable/#/description

## Tags - Medium
# Segment Tree; BinaryIndexed Tree

## Description
# Given an integer array nums, find the sum of the elements between indices i and j( i<=j ), inclusive.
# The update(i, val) function modifies nums by updating the element at index i to val.
# Example:
# Given nums = [1, 3, 5]
# SumRange(0, 2) -> 9; update(1, 2); sumRange(0, 2) -> 8
# NOTE:
# The array is only modifiable by the update function;
# YOu may assume the number of calls to update and sumRange function is distributed evenly.

## Analysis
# For interval/range/segment problems, we takes consideration of segment tree first.
# Segment Tree cost O(N) time to build, O(N) space to store, but O(logN) query and update.

## Solutions
# pythonic way
class NumArray1(object):
    def __init__(self, nums):
        self.nums = nums
    def update(self, i, val):
        self.nums[i] = val
    def sumRange(self, i, j):
        return sum(self.nums[i:j+1])
    
# SegmentTree
class SegmentTree(object):
    def __init__(self, start, end, isum):
        self.start, self.end, self.isum = start, end, isum
        self.left, self.right = None, None
    @classmethod
    def build(cls, nums, start, end):
        if not nums or start > end:
            return None
        root = SegmentTree(start, end, nums[start])
        if start == end:
            return root
        # now start < end
        middle = (start + end) // 2
        root.left = cls.build(nums, start, middle)
        root.right = cls.build(nums, middle+1, end)
        root.isum = root.left.isum + root.right.isum
        return root
    @classmethod
    def update(cls, root, i, val):
        if not root:
	    return
	if root.start == root.end:
	    if root.start == i:
                root.isum = val
            return
        middle = (root.start + root.end) // 2
        if i <= middle:
            cls.update(root.left, i, val)
        else:
            cls.update(root.right, i, val)
        root.isum = root.left.isum + root.right.isum
    @classmethod
    def query(cls, root, start, end):
        if not root or start > end:
            return None
        # out of range
        if root.start > end or root.end < start:
            return None
        # now root.start <= end and root.end >= start
        # segment tree in the range
        if start <= root.start and root.end <= end:
            return root.isum
        left = cls.query(root.left, start, end)
        right = cls.query(root.right, start, end)
        if left is None:
            return right
        if right is None:
            return left
        # now both of them are not None
        return left + right

class NumArray2(object):
    def __init__(self, nums):
        self.root = SegmentTree.build(nums, 0, len(nums)-1)
    def update(self, i, val):
        SegmentTree.update(self.root, i, val)
    def sumRange(self, i, j):
        if not self.root or i > j:
            return None
        return SegmentTree.query(self.root, i, j)

if __name__ == "__main__":
    nums = [1,3,5]
    ans1 = NumArray1(nums)
    ans2 = NumArray2(nums)
    sum1 = ans1.sumRange(0, 2)
    sum2 = ans2.sumRange(0, 2)
    ans1.update(1, 2)
    ans2.update(1, 2)
    sum11 = ans1.sumRange(0, 2)
    sum22 = ans2.sumRange(0, 2)
    if sum1 == sum2 and sum1 == 9 and sum11 == sum22 and sum11 == 8:
        print("Passed: Range Sum Query - Mutable.")
    else:
        print("Failed: Range Sum Query - Mutable.")

    
    


