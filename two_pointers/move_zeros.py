## Reference
# https://www.lintcode.com/problem/move-zeroes/description

## Tags - Easy - Two Pointers/Array - Facebook/Bloomberg

## Description
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations. 

## Example
# Input: nums = [0, 1, 0, 3, 12],
# Output: [1, 3, 12, 0, 0].

# Input: nums = [0, 0, 0, 3, 1],
# Output: [3, 1, 0, 0, 0].

## Solution
# KEY: the slow do not move unless the fast encountered a number
#      then exchange the number with slow, slow ++

class Solution(object):
    # O(N) time; O(1) space
    def moveZeroes1(self, nums):
        if not nums or len(nums) <= 1:
            return
        N = len(nums)
        slow = 0
        for i in xrange(N):
            if nums[i] == 0:
                continue
            nums[slow],nums[i] = nums[i],nums[slow]
            slow += 1
        print nums
        return

    def moveZeroes2(self, nums):
        if not nums or len(nums)<= 1:
            return
        N = len(nums)
        new_nums = [0]*N
        slow = 0
        for num in nums:
            if num == 0:
                continue
            new_nums[slow] = num
            slow += 1
        nums = new_nums
        print nums
        return

if __name__ == "__main__":
    test = Solution()
    nums = [0,1,0,3,12]
    test.moveZeroes1(nums[:])
    test.moveZeroes2(nums[:])





