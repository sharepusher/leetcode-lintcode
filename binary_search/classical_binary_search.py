## Description *
# Find "ANY" postion of a target number in a "SORTED" array. Return -1 if target does not exist.
# Given [1, 2, 2, 4, 5, 5]. For target 2, return 1 or 2.
# For target = 5, return 4, or 5.
# For target = 6, return -1
## Challenge
# O(logN) time

## Solution
# 1) input - sorted array, and a target; 2) ouput - return "ANY" "POSTION", i.e. the index of array
# 3) exception - return -1 if find none; 4) becareful, the index is from 0.
# steps:
#     1) special cases
#     2) binary search - ? how ? compare middle and divide
#     3) find the middle - compare the target with the middle, drop half
#     4) for or while ??? - while, as we need to drop half each time, while is much more convenient 
#     5) when to stop? start + 1 < end: i.e. stop when end appears next to the start; handle that 
#        in a seperate conditon. 

import sys
class Solution:
    def findPosition(self, A, target):
        # handle special cases: A is empty or None, target is None
        if not A or target is None:
            return -1
        N = len(A)
        start, end = 0, N-1
        while start + 1 < end:
            middle = (start+end) // 2
            if A[middle] == target:
                return middle
            if A[middle] < target:
                # target should be in the right part, drop the left
                start = middle
            else:
                end = middle
        # handle start + 1 = end
        # what if only one item in the list, in this case, start == end
        #  
        if A[start] == target:
            return start
        if A[end] == target:
            return end
        return -1

if __name__ == "__main__":
    A = [1, 2, 2, 4, 5, 5]
    target1, target2, target3 = 2, 5, 6
    ans = Solution()
    if ans.findPosition(A, target1) in (1, 2) or ans.findPosition(A, target2) in (4, 5):
        print("find the target!")
    else:
        print("failed to find the target!")
        sys.exit()      
    if ans.findPosition(A, target3) == -1:
        print("passed the test")
     
   
