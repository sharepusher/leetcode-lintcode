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
# How? 


## Solution
class Solution:
    ## Brute force
    def findMin(self, num):
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

if __name__ == "__main__":
    ans = Solution()
    num = [4, 4, 5, 6, 7, 0, 1, 2]
    if ans.findMin(num) == 0:
        print("[Passed] - Find minimum in rotated sorted array2") 
    else:    
        print("[Failed] - Find minimum in rotated sorted array2") 





