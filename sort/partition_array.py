## Reference
# http://www.lintcode.com/en/problem/partition-array/#

## Tags - Medium
# Quik Sort; Two Pointers; Array

## Description
# Given an array nums of integers and an int k, partition the array(i.e move the elements in "nums")
# such that:
# 1) all elements < k are moved to the left
# 2) all elements >= k are moved to the right
# Return the partition index, i.e. the first index i nums[i]>=k.
# NOTE:
# You should do really partition in array nums instead of just counting the numbers of integers smaller
# than K.
# If all elements in nums are smaller than k, then return nums.length
# Example:
# If nums=[3,2,2,1] and k=2, a valid answer is 1.

## Analysis
# input - array of integers; int k
# output None - the first index i that nums[i] >= k
# corner case, if no item, return 0 according to the notice.
# Two pointers

## Solution
class Solution:
    def partitionArray(self, nums, k):
        if not nums:
	    return 0
        N = len(nums)
        start, end = 0, N-1
        while start <= end:
            while start <=end and nums[start] < k:
                start += 1
            while start <= end and nums[end] >= k:
                end -= 1
            if start <= end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        return start 

if __name__ == "__main__":
    nums = [3, 2, 2, 1]
    k = 2
    ans = Solution()
    if ans.partitionArray(nums, k) == 1:
        print("Passed: Partition Array.")
    else:
        print("Failed: Partition Array.")
            



