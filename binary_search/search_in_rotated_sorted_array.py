## Reference
# http://www.lintcode.com/en/problem/search-in-rotated-sorted-array/

## Tags - Medium
# Binary Search


## Description
# Suppose a sorted array is rotated at some pivot unknown to you beforehand
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2)
# You are given a target value to search.
# If found in the array return its index, otherwise return -1.
#
# Notice: assume no duplicate exists.
#


## Challenge
# O(logN) time

## Analysis
# There are two kind of middle values in the problem.
# 1) The middle is located at the first part, 
# 2) the middle is dropped on the second part
#  
# brute force is the basic solution; but it's time complexity is O(N)
# binary search is a little bit special in rotated sorted array
# we need to use start and end element to define which situation
# Comparing the A[middle] and target is not enough to locate which situation
# the middle is on.
# we can only use the binary search on a sorted array range, but not the entire
# rotated array.
# How:  
#    1) if A[middle] == target: then the middle is the index looking for;
#    2) if A[middle] < target: i.e target is in the right part
#        then there are two cases
#        a. the middle is in the second part or the middle is in the original array
#            
#           as A[middle] <= target <= A[end]
#        b. 
#
# 

## Solution
class Solution:
    ## brute force - O(N) time
    def search1(self, A, target):
        if not A or target is None:
            return -1
        N = len(A)
        for i in xrange(N):
            if A[i] == target:
                return i
        return -1           

    ## binary search - O(logN) time
    def search2(self, A, target):
        if not A or target is None:
            return -1
        N = len(A)
        start, end = 0, N-1
        while start + 1 < end:
            middle = (start+end) // 2
            if A[middle] == target:
                return middle
            # A[middle] > or < target
            if A[start] < A[middle]:
                # situation 1: it's in the original sequence or the 1st half
                # and start might equal target
                if A[start] <= target <= A[middle]:
                    end = middle
                else:
                    start = middle
            else:
                # situation2:
                # it lies in the second part
                # there's two cases in the second part
                if A[middle] <= target <= A[end]:
                    start = middle
                else:
                    end = middle
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1
          
if __name__ == "__main__":
    a = [4, 5, 1, 2, 3]
    t1, ret1 = 1, 2
    t2, ret2 = 0, -1
    ans = Solution()
    if ret1 == ans.search2(a, t1) and ret2 == ans.search2(a, t2) \
       and ret1 == ans.search1(a, t1) and ret2 == ans.search1(a, t2):
        print("[Passed] - Search in Rotated Sorted Array")
    else:
        print("[Failed] - Search in Rotated Sorted Array")

