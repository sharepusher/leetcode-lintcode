## Reference
# https://leetcode-cn.com/problems/height-checker/
# https://blog.csdn.net/chouisbo/article/details/54906909

## Easy - HammingDistance/Sort

## Descriptin
# Students are asked to stand in non-decreasing order of heights for an annual photo.
# REturn the minimum number of students not standing in the right positions.
# This is the number of students that must move in order for all students to be standing in non-decreasing order of height.
## 1 <= heights.length <= 100
## 1 <= heights[i] <= 100

## Example
# Input: [1,1,4,2,1,3]
# Output: 3
# Explanation: 
# Students with heights 4, 3 and the last 1 are not standing in the right positions.

## Analysis
# Hamming Distance between array

## Solution
class Solution(object):
    def heightChecker(self, heights):
        if not heights or len(heights) <= 1:
            return 0
        #return sum(h1!=h2 for h1,h2 in zip(heights, sorted(heights)))
        #return len(filter(lambda (x1,x2): x1!=x2, zip(heights, sorted(heights)))
        N = len(heights)
        counter = 0
        new_heights = sorted(heights)
        for i in xrange(N):
            if heights[i] == new_heights[i]:
                continue
            counter += 1
        return counter






