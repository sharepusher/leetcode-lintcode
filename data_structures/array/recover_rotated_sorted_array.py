## Reference
# http://www.lintcode.com/en/problem/recover-rotated-sorted-array/#

## Tags - Easy
# Sorted Array

## Description
# Given a rotated sorted array, recover it to sorted array in-place
# What is rotated array?
# For example, the original is [1,2,3,4], the rotated array can be [1,2,3,4], [2,3,4,1],[3,4,1,2]
# Example: [4,5,1,2,3]=>[1,2,3,4,5]

## Challenge
# In-place, O(1)extra space and O(N) time.

## Analysis
# The key is find the rotated point, how? traverse the entire array
# And then rotate in 3 steps?
# NO duplicates ?

## Solution
class Solution:
    def recoverRotatedSortedArray1(self, nums):
        if not nums:
            return nums
        # find the rotate point
        N = len(nums)
        # iterate in reverse order
        for i in xrange(N-1):
            if nums[i] > nums[i+1]:
                # this will be the roate point
                nums[:] = nums[i+1:] + nums[:i+1]
                #nums[i+1:], nums[:i+1] = nums[:i+1], nums[i+1:]
                break
        return
    def reverse(self, nums, start, end):
        if not nums or start > end:
            return
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        return

    def recoverRotatedSortedArray2(self, nums):
        if not nums:
            return nums
        N = len(nums)
        for i in xrange(N-1):
            if nums[i] > nums[i+1]:
                # reverse
                self.reverse(nums, i+1, N-1)
                self.reverse(nums, 0, i)
                self.reverse(nums, 0, N-1)
                break
        return

if __name__ == "__main__":
    nums1 = [4, 5, 1, 2, 3]
    result = [ 1, 2, 3, 4, 5]
    nums2 = [5, 1, 2, 3, 4]    

    ans = Solution()
    ans.recoverRotatedSortedArray1(nums1) 
    ans.recoverRotatedSortedArray2(nums2)
    if nums1 == result and nums2 == result:
        print("Passed: Recover Rotated Sorted Array.")
    else:
        print("Failed: Recover Rotated Sorted Array.")
        





