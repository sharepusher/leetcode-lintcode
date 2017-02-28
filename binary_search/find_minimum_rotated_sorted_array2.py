## Reference
# http://www.lintcode.com/en/problem/find-minimum-in-rotated-sorted-array-ii/

## Tags - Medium 
# Binary Search; Divide and Conquer

## Description
# Suppose a sorted array is rotated at some pivot unkonwn to you beforehand.
# (i.e. 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2)
# Find the minimum element
#
# NOTICE: The array may contain duplicates.
#


## Analysis
# compared with first problem, we need to handle the duplicates
#
#  The worse case is that if all the numbers are the same, then binary search doesn't work
#  The only solution is O(N) traversal !!!
#  Therefore, actually, this case means that we cannot handle it with binary search totally
# 
#
# 1) brute force, no matter there's duplicates or not.
# 2) binary search
#    as duplicates, the start and end may be equal, in this case, num[start] >= num[[end]
#    it's hard to covere the two cases, and hard to differetiate them
#    a. if pivot is num[start], 
#      then, it's impossible to meet the requirement that 
#      dropping the greater part in sorted array and dropping the smaller part in the rotated array
#    b. if pivot is num[end], we need to drop the greater part
#       Which can fullfill the requirement of the two cases
# 


## Solution
class Solution:
    ## Brute force - O(N) time, O(1) space
    def findMin1(self, num):
        if not num:
            return None
        N = len(num)
        if N == 1:
            return num[0]
        min_num = num[0]
        for item in num:
            if item < min_num:
                min_num = item
        return min_num

    def findMin2(self, num):
        if not num:
            return None
        N = len(num)
        if N == 1:
            return num[0]
        start, end = 0, N-1
        min_num = num[end]
        while start + 1 < end:
            middle = (start + end) // 2
            if num[middle] == min_num:
                # in this case, NO better way to drop any part, but just reduce the range by
                # If middle equals to the end, which means it's fine to remove end,
                # as in this case, the smallest won't be removed unexpectedly.
                end -= 1
            elif num[middle] > min_num:
                start = middle
            else:
                # num[middle] <
                end = middle
        return min(num[start], num[end], min_num)

if __name__ == "__main__":
    ans = Solution()
    num = [4, 4, 5, 6, 7, 0, 1, 2]
    if ans.findMin1(num) == 0 and ans.findMin2(num) == 0:
        print("[Passed] - Find minimum in rotated sorted array2") 
    else:    
        print("[Failed] - Find minimum in rotated sorted array2") 





