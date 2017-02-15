## Reference
http://www.lintcode.com/en/problem/first-position-of-target/#

## Description
# For a given sorted array (ascending order) and a target number, find the FIRST index of this number in O(logN) time complexity.
# If the target number does not exist in the array, return -1.

## Challenge
# If the count of numbers is bigger than 2^32, can your code work properly?

## Analysis
# input - SORTED ARRAY, target; output - index(FIRST position the target appears!)
# exception: return -1
# steps:
# 1) sorted array;
# 2) find the target, how to find the first position? AS it's sorted array
#    a. binary search can find any position of the target
#    b. then check whether it's the first/left most one? how? another while???
#       NO, in this case, we only need continue the original while loop,
#       The DIFFERENCE is that whenever we find the target, we make it as the end!
#       why? for example, we have 3 same numbers, then if we wanna find the left most target, only middle=end
#       

## Solution

class Solution:
    def binarySearch(self, nums, target):
        if not nums or target is None:
            return -1
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            middle = (start+end) // 2
            if nums[middle] == target:
                # we need check whether it's the left most one by label middle as end
                end = middle
            elif nums[middle] < target:
                start = middle
            else:
                end = middle
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1

if __name__ == "__main__":
    nums = [1, 2, 3, 3, 4, 5, 10]
    target = 3
    nums2 = [1, 4, 4, 5, 7, 7, 8, 9, 9, 10]
    target2 = 1
    ans = Solution()
    if ans.binarySearch(nums, target) == 2 or ans.binarySearch(nums2, target2):
        print("passed test") 
    else:
        print("failed test")


