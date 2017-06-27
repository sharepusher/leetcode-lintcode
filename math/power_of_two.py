## Reference
# 231 https://leetcode.com/problems/power-of-two/#/description
# http://www.lintcode.com/en/problem/o1-check-power-of-2/

## Description
# Given an integer, write a function to determin if it is a power of two.

## Challenge
# O(1) time and space.

## Analysis
# 2^X = N => 2*2*2....= N
# Power: a mathematical notation indicating the number of times a quantity is multiplied by itself.
# The power of 2 is composed by 1 and 0 in binary, 

## Solution
class Solution(object):
    # modular and division
    # time O(logN), O(1) space
    def isPowerOfTwo1(self, n):
        if not n or n < 1:
            return False
        while n % 2 == 0:
            n //= 2
        return n == 1

    # bit operation
    # O(1) time and space
    def isPowerOfTwo2(self, n):
        if not n or n <= 0:
            return False
        return n & (n-1) == 0

if __name__ == "__main__":
    ans = Solution()
    if ans.isPowerOfTwo1(1) and ans.isPowerOfTwo2(1) and ans.isPowerOfTwo1(2) and ans.isPowerOfTwo2(2):
        print("Passed: Power of two.")
    else:
	print("Failed: Power of two.")

