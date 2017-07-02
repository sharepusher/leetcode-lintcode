## Reference
# 201 https://leetcode.com/problems/bitwise-and-of-numbers-range/#/description

## Description
# Given a range [m, n] where 0 <=m<=n<=2147483647, return the bitwise AND of all numbers in this range, inclusive.
# For example, given the range[5, 7], you should return 4.

## Analysis
# 1) broute-force
# 2) power of two
# 3) the characters of binary representation

## Solution
class Solution(object):
    # brute-force
    # O(N)-Time; O(1)space
    def rangeBitwiseAnd1(self, m, n):
        # corner case
        if m < 0 or n <= m:
            return None
        if m == 0:
            return m
        # now m > 0 and n > m
        ret = m
        for i in xrange(m+1, n+1):
            ret &= i
        return ret

    # power of two character: the power of two in binary representation will be all zero except the first one
    # And the N-1 will be all one except the first 0, therefore, N&(N-1) will be 0.
    # If there's a number of power of two in the range, then it will be 0.
    # or we count the range & 
    def rangeBitwiseAnd2(self, m, n):
        if m < 0 or n <= m:
            return None
        if m == 0:
            return m
        # check whether power of two in the range
        start = 2
        while start <= m:
            start *= 2
        if start <= n:
            return 0
        # now no power of two in the range
        ret = m
        for i in xrange(m+1, n+1):
            ret &= i
        return ret
        
    # The result is the common prefix of m and n(non-negative)
    # The key is we think the number in binary representation, but not in decimal system.
    # In other words, say the number range is from 110101001 to 110110010
    # if m!=n, the consequtive numbers will always different. i.e. if they are consequtive number,
    # then the last digit of even number will be 0, and the odd will be 1, in this case the & result is 0.
    # therefore, the final result last digit is also 0.
    # No only the last digit, the middle part of the range in the consequtive sequence will be different 
    # therefore, the & result is also 0, only the common prefix left after the & operation.
    def rangeBitwiseAnd3(self, m, n):
        if m < 0 or n <= m:
            return None
        if m == 0:
            return m
        zbits = 0
        while m != n:
            m >>= 1
            n >>= 1
            zbits += 1
        return m << zbits
    # recursion 
    def rangeBitwiseAnd4(self, m, n):
        if m < 0 or n <= m:
            return None
        if m == 0:
            return 0
        return self.rangeBitwiseAnd4(m//2, n//2) << 1 

if __name__ == "__main__":
    ans = Solution()
    if ans.rangeBitwiseAnd1(1,5) == ans.rangeBitwiseAnd2(1, 5) and ans.rangeBitwiseAnd3(1,5) == ans.rangeBitwiseAnd4(1,5):
        print("Passed: Bitwise And of number Range.")
    else:
        print("Failed: Bitwise And of number Range.")



