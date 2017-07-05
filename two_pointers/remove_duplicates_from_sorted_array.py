## Reference
# 26 https://leetcode.com/problems/remove-duplicates-from-sorted-array/#/solutions
# http://www.lintcode.com/en/problem/remove-duplicates-from-sorted-array/

## Tags - Easy; Red
# Two Pointers; Sorted Array; Facebook.

## Description
# Given a sorted array, remove the duplicates in place 
# such that each element appear only once and Return the new length.
# Do NOT allocate extra space for another array, you must do this in place with constant memory.
# Example:
# Given input array A = [1,1,2]
# Your function should return length = 2, and A is now[1,2]
# It doesn't matter what you leave beyound the new length.

## Analysis
# O(1)-space => in-place update => pointers => fast-slow pointers
# As it's sorted, the duplicates will be adjacent.
# KEY: the slow will be start from 0, therefore, return should be slow + 1

## Solution
class Solution(object):
    def removeDuplicates1(self, nums):
        if not nums:
            return 0 
        N = len(nums)
        if N == 1:
            return 1
        slow, fast = 0, 0
        while fast < N:
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
            fast += 1
        return slow + 1 

    def removeDuplicates2(self, nums):
        if not nums or len(nums) == 1:
            return len(nums)
        N = len(nums)
        slow = 0
        for fast in xrange(N):
            if nums[fast] != nums[slow]:
                slow += 1
                nums[slow] = nums[fast]
        return slow + 1

if __name__ == "__main__":
    ans = Solution()
    nums = [1, 1, 2]
    if ans.removeDuplicates1(nums) == 2 and ans.removeDuplicates2(nums) == 2:
        print("Passed: remove duplicates from sorted array.")
    else:
        print("Failed: remove duplicates from sorted array.")
