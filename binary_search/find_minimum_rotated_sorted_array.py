## Reference
# http://www.lintcode.com/en/problem/find-minimum-in-rotated-sorted-array/#

## Tags - Medium
# Binary Search

## Description
# Suppose a sorted array is rotated at some pivot unknown to you beforehand

## Analysis
#   input - Sorted, rotated array
#      1) normal order( all the same element); 2) decending order; 
#      3) typical rotated order    
#   ouput - minumum element
#   exception:
#       [] - None
#   steps:
#      1) brute force O(N):
#          traverse - one min temp to record the minimal
#      2) binary search - sorted array, rotated?
#         # the rotate here is not reverse, it will keeep its original order
#         # no duplicate -
#         # therefore, two cases
#         1) keep the original order num[-1] is always >=num[0]
#         2) the first part is always greater than the second part



## Solution
class Solution:
    # Brute force - O(N)
    # traverse - index traverse; value traverse? which one? do we need index?
    # no index needed, just need verify the value, so iterat value directly
    def findMin1(self, num):
        if not num:
            return None
        # init the min
        import sys 
        min_num = sys.maxint
        for item in num:
            if min_num > item:
                min_num = item
        return min_num
    # 
    # binary search 
    # find the first position that smaller than num[0]
    def findMin2(self, num):
        if not num:
            return None
        N = len(num)
        # original sorted array
        if num[0] <= num[-1]:
            return num[0]

        # the rotated array
        # as no duplicate, find the first position that smaller than the num[0]
        min_num = num[0]
        start, end = 0, N-1
        while start + 1 < end:
            middle = (start+end) // 2
            if num[middle] >=  min_num:
                start = middle
            else:
                end = middle
        if num[start] < min_num:
            return num[start]
        if num[end] < min_num:
            return num[end]
        return min_num
        
        # binary search
        # Find the first position that smaller than last item
    def findMin3(self, num):
        if not num:
            return None
        N = len(num)
        # first situation
        if num[0] < num[-1]:
            return num[0]
        # second situation
        start, end = 0, N-1
        min_num = num[-1]
        while start + 1 < end:
            middle = (start + end) // 2
            if num[middle] >= min_num:
                start = middle
            else:
                end = middle
        if num[end] < min_num:
            return num[end]
        if num[start] < min_num:
            return num[start]
        return min_num            





       
if __name__ == "__main__":
    num = [4, 5, 6, 7, 0, 1, 2]
    ans = Solution()
    if 0 == ans.findMin1(num) and ans.findMin2(num) == 0 and 0 == ans.findMin3(num):
        print("[Passed] - find minimum in rotated sorted array")
    else:
        print("[Failed] - find minimum in rotated sorted array")

