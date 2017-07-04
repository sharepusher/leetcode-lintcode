## Reference
# http://www.lintcode.com/en/problem/search-in-rotated-sorted-array-ii/
# 81 https://leetcode.com/problems/search-in-rotated-sorted-array-ii/#/description

## Tags - Medium; Blue
# Binary Search; Sorted Array

## Description
# Follow up for Search in Rotated Sorted Array.
# What if duplicates are allowed?
# Would this affect the run-time complexity? How and Why?

# Write a function to determin if a given targets is in the array.

## Analysis
# Though it's a follow up questions, it just ask whether the target exist or not !
#  But NOT its index if it's in, as it may be many chocies for the same target,
#  for similar questions, they may ask to return any of them.
#  As duplicates exist, we cannot distinguish where is the sorted array started or ended.
#  therefore, increment or decrement start/end is the only way to narrow the hunting circle
#  Based on the inital problem, A[end] <= A[middle] to distingui it in two part

## Solution
class Solution:
    # brute force - O(N)
    def search1(self, A, target):
        if not A or target is None:
            return False
        N = len(A)
        for i in xrange(N):
            if A[i] == target:
                return True
        return False

    def search2(self, A, target):
        if not A or target is None:
            return False
        N = len(A)
        start, end = 0, N-1
        while start + 1 < end:
            middle = (start+end) // 2
            if A[middle] == target:
                return True
            if A[end] == A[middle]:
                end -= 1
            elif A[end] > A[middle]:
                if A[middle] < target <= A[end]:
                    start = middle
                else:
                    end = middle
            else:
                # A[middle] > A[end], the first part
                if A[start] <= target < A[middle]:
                    end = middle
                else:
                    start = middle
        if A[start] == target or A[end] == target:
            return True
        return False
           

if __name__ == "__main__":
    ans = Solution()
    a1 = [1, 1, 0, 1, 1, 1]
    t1, ret1 = 0, True
    a2 = [1, 1, 1, 1, 1, 1, 1]
    t2, ret2 = 0, False 
    if ans.search2(a1, t1) == ret1 and ans.search2(a2, t2) == ret2 \
       and ans.search1(a1, t1) == ret1 and ans.search1(a2, t2) == ret2:
        print("[Passed] - Search in Rotated Sorted Array 2")
    else: 
        print("[Failed] - Search in Rotated Sorted Array 2") 
