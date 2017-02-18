## Reference
# http://www.lintcode.com/en/problem/search-a-2d-matrix/

## Tag
# Easy - Matrix

## Description
# Write an efficient algorithm that searches for a value in an mxn matrix.
# This matrix has the following properties:
#  1) Integers in each row are sorted from left to right.
#  2) The first integer of each row is greater than the last integer of the previous row.

## Challenge
# O(logN+longM) time

## Analysis
#  input - a sorted 2d integer matrix, an integer target;
#    the matrix first integer of each row is greater than the last integer of the previous row. 
#  output - True/False or return the position(index)
#  exception - empty matrix, False/None
#      how about the input is 1d array but not a matrix
# steps:
#    1) find the last row that smaller and equal than the target by binary search 
#    2) find the target in the row by binary search

## Solution
class Solution:
   
    def binarySearch(self, array, target):
        if not array or target is None:
            return False
        N = len(array)
        start, end = 0, N
        while start + 1 < end:
            middle = (start + end) // 2
            if array[middle] == target:
                return (True, None)
            if array[middle] < target:
                start = middle
            else:
                end = middle
        if array[start] == target:
            return (True, None)
        if array[end] == target:
            return (True, None)
        if array[end] < target:
            return (False, end)
        elif array[start] < target:
            return (False, start) 
        else:
            return (False, None)

    def searchMatrix1(self, matrix, target):
        # corner case
        if not matrix or target is None:
            return False
        if len(matrix) == 1:
            result = self.binarySearch(matrix[0], target)
            return result[0]
        M, N = len(matrix), len(matrix[0])
        

    def searchMatrix(self, matrix, target):
        # corner case
        if not matrix or target is None:
            # return None  # if query index
            return False
        # find the target row 
        M, N = len(matrix), len(matrix[0]) # row, column
        start, end = 0, M-1
        while start + 1 < end:
            middle = (start + end) // 2
            if matrix[middle][0] == target:
                return True
            elif matrix[middle][0] < target:
                start = middle
            else:
                end = middle
        if matrix[start][0] == target:
            return True
        if matrix[end][0] == target:
            return True
        if matrix[end][0] < target:
            row_start = end
        elif matrix[start][0] < target:
            row_start = start
        else:
            return False

        # becareful the index, N-1 NOT N
        start, end = 0, N-1
        while start + 1 < end:
            middle = (start + end) // 2
            if matrix[row_start][middle] == target:
                return True
            if matrix[row_start][middle] < target:
                start = middle
            else:
                end = middle
        if matrix[row_start][start] == target:
            return True
        if matrix[row_start][end] == target:
            return True
        return False

if __name__ == "__main__":
    matrix = [[1, 3, 5, 7],[10, 11, 16, 20], [23, 30, 34, 50]]
    target = 3
    ans = Solution()
    if ans.searchMatrix(matrix, target):
        print("test pass")
    else:
        print("test failed")        

