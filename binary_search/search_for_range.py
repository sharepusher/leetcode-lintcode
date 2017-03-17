## Reference
# http://www.lintcode.com/en/problem/search-for-a-range/#


## Tags - Medium
# Binary Search; Sorted Array; Array


## Description
# Given a sorted array of N integers, find the starting and ending position of a given target value.
# If the target is not found in the array, return [-1, -1]
# Example:
# Given [5, 7, 7, 8, 8, 10] and target value 8, return [3, 4]


## Analysis
# input - @param A: the list of integers;
#         @param target: an integer to be searched
# output - @return: a list of length 2, [start_index, end_index]
#
# first, it's a sorted array, so we can use the binary search
# the naive solution is find the first target, and then find the last target
# the better one is that we find the target first, and then do the index-- and index ++ to find 
# the start and end index.
# How: find the index, break; while index > 0: index --; while index < N: index ++
# BUT, when the worse case, it will cost O(N) (i.e. A is full of the same item)
# Therefore, the better solution is two binary search to determin the lower bound and upper bound.
# 


## Solution
class Solution:
    # Time - O(N); Space - O(1)
    #  traverse the array, find the target and then the range by end ++ 
    def searchRange1(self, A, target):
        # corner case
        if not A or target is None:
            return [-1, -1]
        # init start, end index
        start, end = -1, -1
        # traverse the array
        for k, v in enumerate(A):
            if target == v:
                # update start AND END, Both of them HAVE TO BE UPDATED, 
                # as maybe only one item
                # additionally, we need check the end range later
                start, end = k, k
                break
        # end should < N-1, or there will be out of range when testing end+1
        while end < len(A)-1:
            # we need to check the end + 1, BUT not end, or it will quit unexpected
            if A[end+1] != target:
                break
            end += 1
        return [start, end]
    
    # binary search
    # worse case O(N)
    def bSearch(self, A, target):
        if not A or target is None:
            return -1
        N = len(A)
        start, end = 0, N-1
        while start + 1 < end:
            middle = (start + end) // 2
            if A[middle] == target:
                return middle
            if A[middle] < target:
                start = middle
            else:
                end = middle
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1


    def searchRange2(self, A, target):
        if not A or target is None:
            return [-1, -1]
        index = self.bSearch(A, target)
        if index == -1:
            return [index, index] 
        start, end = index, index
        while start > 0:
            if A[start-1] != target:
                break
            start += 1
        while end < len(A)-1:
            if A[end+1] != target:
                break
            end += 1
        return [start, end]

    # find the first position(lower bound) of target by binary search
    def lbSearch(self, A, target):
        N = len(A)
        start, end = 0, N-1
        while start+1 < end:
            middle = (start+end) // 2
            if A[middle] >= target:
                 end = middle
            else:
                 start = middle
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1
    # find the last position of target
    def ubSearch(self, A, target):
        N = len(A)
        start, end = 0, N-1
        while start+1 < end:
            middle = (start+end) // 2
            if A[middle] <= target:
                start = middle
            else:
                end = middle
        if A[end] == target:
            return end
        if A[start] == target:
            return start
        return -1


    def searchRange3(self, A, target):
        if not A or target is None:
            return [-1, -1]
        return [self.lbSearch(A, target), self.ubSearch(A, target)]         
 
if __name__ == "__main__":
    A = [5, 7, 7, 8, 8, 10]
    target = 8
    ans = Solution()
    if ans.searchRange1(A, target) == [3, 4] and \
       ans.searchRange2(A, target) == [3, 4] and \
       ans.searchRange3(A, target) == [3, 4]:
        print("[Passed] - Search For a Range.")
    else:
        print("[Failed] - Search For a Range.")
 
