## Reference
# http://www.lintcode.com/en/problem/rotate-image/
# 48 https://leetcode.com/problems/rotate-image/#/description

## Tags - Medium; Blue
# CrackingTheCodingInterview; Matrix

## Description
# You are given an nxn 2D matrix representing an image.
# Rotate the image by 90 degree(clockwise).
# Example:
# Given a matrix 
# [[1,2],[3,4]] => [[3,1],[4,2]]

## Challenge
# Do it in-place

## Analysis
# The characteristc of the matrix rotate, is that row and colum exchange, and then reverse row
# exchange row and column entire need extra space
# exchange one by one can save make it in-place

## Solution
class Solution:
    def rotate(self, matrix):
        if not matrix:
            return
        N = len(matrix)
        for i in xrange(N):
            for j in xrange(i+1, N):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # reverse row
        for i in xrange(N):
            matrix[i].reverse()
        return
if __name__ == "__main__":
    matrix = [[1,2],[3,4]]
    rematrix = [[3,1],[4,2]]
    ans = Solution()
    ans.rotate(matrix)
    if matrix == rematrix:
        print("Passed: Rotate Image.")
    else:
        print("Failed: Rotate Image.")




