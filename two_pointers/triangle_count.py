## Reference
# https://www.lintcode.com/problem/triangle-count/description

## Medium - TwoPointer

## Description
# Given an array of integers, how many three numbers can be found in the array, 
# so that we can build an triangle whose three edges length is the three numbers that we find?

## Example
# Input: [3, 4, 6, 7]
# Output: 3
# Explanation:
# They are (3, 4, 6), 
#         (3, 6, 7),
#         (4, 6, 7)

# Input: [4, 4, 4, 4]
# Output: 4
# Explanation:
# Any three numbers can form a triangle. 
# So the answer is C(3, 4) = 4

## Solution
# KEY - 1) how to form a triangle with 3 edges? The requirement: any of 2 edges should be greater than the other edge
# in this case, there's 3 condition that have to be meet, say, A,B,C, then A+B > C, B+C > A, A+C >B
# But is the list is sort, the problem will be simpler, as we only need prove one condition A+B>C (A<B<C)
# As B+C > A and A+C > B is obvious, no necessary to prove.
# 2) how to count? 3sum

# 1. O(N^3)
class Solution(object):
    def triangleCount(self, S):
        if not S or len(S) < 3:
            return 0
        N = len(S)
        # key: SORT !!!!
        S.sort()
        total = 0
        for i in xrange(N-2):
            # key: i+1, j+1, and i < j < k
            for j in xrange(i+1, N-1):
                for k in xrange(j+1, N):
                    if S[i]+S[j] <= S[k]:
                        break
                    total += 1
        return total

# 2. O(N^2) 3Sum
    def triangleCount2(self, S):
        if not S or len(S) < 3:
            return 0
        N = len(S)
        # key: SORT!!!
        S.sort()
        total = 0
        for k in xrange(2, N):
            left, right = 0, k-1
            while left < right:
                current = S[left]+S[right]
                if current <= S[k]:
                    left += 1
                else:
                    # key: all the number pair between left and right are valid
                    # (left,right)(left+1,right)... (left+m,right)
                    total += (right-left)
                    right -= 1
        return total


s = Solution()
S = [5, 3, 4, 6, 7]
if s.triangleCount(S) == s.triangleCount2(S):
    print "pass"
else:
    print "fail"


