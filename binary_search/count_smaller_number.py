## Reference
# http://www.lintcode.com/en/problem/count-of-smaller-number/#

## Tags
# Binary Search; Segment Tree

## Challenge
# Three ways to do it
# 1) just loop
# 2) sort and binary search
# 3) build segment tree and search

## Description
# Give you an integer array (index from 0 to n-1, where n is the size of this array, value from 0 to 10000)
# and an query list. 
# For each query, give you an integer, return the number of element in the array that are smaller than the given integer.


## Analysis
# input - integer Array; queries; output - array: counted number
# Exception - empty array or filled with 0

# Brute force M*N
#  1) becareful the corner case is special on return
#  2) nested loop

# binary search
#  1) sort first
#  2) last position that smaller than the target
#  3) visited hash table can save time for duplicated queries by more space consuming

# segment tree
#  TO BE continued

class Solution:
    # binary search - O((M+N)logN)
    def countOfSmallerNumber(self, A, queries):
        if not A or not queries:
            return [0] * len(queries)
        # sort first
        A.sort()
        visited = {}
        result = []
        for que in queries:
            if que in visited:
                result.append(visited[que])
                continue
            # binary search for not visited ones
            index = self.bSearch(A, que)
            counter = 0
            if index != -1:
                counter = index + 1
            result.append(counter)
    
        return result
    # binary search to find out the last position that smaller than the target
    # input - integer array, target; output - index, -1(if not found)
    def bSearch(self, A, target):
        if not A or target is None:
            return -1
        N = len(A)
        start, end = 0, N-1
        while start + 1 < end:
            middle = (start + end) // 2
            if A[middle] >= target:
                # cut off the big one
                end = middle
            else:
                start = middle
        if A[end] < target:
            return end
        if A[start] < target:
            return start
        return -1

    # brute force
    def countOfSmallerNumber1(self, A, queries):
        # corner case
        if not A or not queries:
            return [0] * len(queries)
        result = []
        for que in queries:
            counter = 0
            for num in A:
                if num < que:
                    counter += 1
            result.append(counter)
        return result

if __name__ == "__main__":
    A = [1, 2, 7, 8, 5]
    queries = [1, 8, 5]
    result = [0, 4, 2]

    ans = Solution()
    if ans.countOfSmallerNumber(A, queries) == result:
        print("[pass] - count of smaller numbers")
    else:
        print("[fail] - count of smaller numbers")        
   
