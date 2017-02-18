## Reference
# http://www.lintcode.com/en/problem/search-insert-position/

## Tags
# Easy - Binary Search

## Description
# Given a sorted array and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You may assume NO duplicates in the array.
# 

## Challenge
# O(logN) time

## Analysis
#   input - sorted array, target;
#   output - target index or the inserting index; i.e. last index that smaller and equal to the target
#   exception - empty array, return 0; 
#      Becareful - For empty array, as they can NOT be treated properly by binary search, NO end in that case
#      therefore, we should handle that case before binary search processing !!!!!!
#   steps:
#       1) brute force: traverse the entire array, and return the index
#            a for or while loop, find the first item equal to the target or greater than the target
#       2) binary search: last smaller or first greater??? either of them should be fine.
#              

## Solution
class Solution:
    # Brute force - O(N)
    # find the first postion that greater than the target!
    # if find the target return the index
    # if find the first greater one, then the target should REPlACE IT, then still return the index
    # so we can merge them !!!!!
    def searchInsert1(self, A, target):
        if A is None or target is None:
            return None
        N = len(A)
        for i in xrange(N):
            if A[i] >= target:
                return i
        # for those out of the range or empty array
        return N
   
    # sorted array -> binary search: O(logN) 
    #    last position that smaller and equal to the target
    #    or first position that equal and greater than the target
    def searchInsert(self, A, target):
        if A is None or target is None:
            return None
        N = len(A)
        if N == 0:
            return 0
        # binary search can handle one item array, as in that case, start == end == 0
        # both of them won't cause the index out of range error ! 
        start, end = 0, N-1 
        while start + 1 < end:
            middle = (start + end) // 2
            if A[middle] == target:
                return middle
            if A[middle] < target:
                start = middle
            else:
                end = middle
        if A[end] < target:
            return end + 1
        if A[start] < target:
            return start + 1
        # all of them greater than the target, then insert to the first one 
        return start 
    

if __name__ == "__main__":
    a1 = [1, 3, 5, 6]
    t1, t2, t3, t4 = 5, 2, 7, 0
    ans = Solution()
    if 2 == ans.searchInsert(a1, t1) and \
       1 == ans.searchInsert(a1, t2) and \
       4 == ans.searchInsert(a1, t3) and \
       0 == ans.searchInsert(a1, t4):
        print("test passed")
    else:
        print("test failed xxxxxx")
