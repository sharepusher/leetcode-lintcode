## Reference
# http://www.lintcode.com/en/problem/powx-n/

## Tags
# Medium

## Description
# Implement pow(x, n)
# Pow(2,1, 3) = 9.261
# Pow(0, 1) = 0
# Pow(1, 0) = 1

## Challenge
# O(logN) time

## Analysis
# Input - base number in double, power number int; Output - the result in double
# special cases: n == 0, n == 1, n is negtive
# steps:
#     1) handle specail cases 
#     2) while loop to repeat the multiple calculation(brute force)
#     3) or the recursion way to divide N
#        a. divide calculate the x**(n/2), and then multiple the values


## Solution
class Solution:
    # divide and conquer / binary search
    def pow(x, n):
        # base case
        if n == 0:
            return 1
        if n == 1:
            return x
        # divide
        value = self.pow(x, n//2)
        # conquer
        if n % 2 == 0:
            return value * value
        else:
            return value * value * x

    def myPow3(self, x, n):
        # corner case
        if n == 0 or x == 1:
            return 1
        if n == 1 or x == 0:
            return x
        if n < 0:
            return 1 / self.pow(x, -n)
        else:
            return pow(x, n) 
 

    # brute force
    def myPow2(self, x, n):
        if n == 0 or x == 1:
            return 1
        if n == 1 or x == 0:
            return x
        neg_flag = False
        if n < 0:
            neg_flag = True
            n = -n
        # init the intermediary
        ans = x
        while n > 1:
            ans *= x
            n -= 1
        if neg_flag:
            return 1 / ans
        return ans
    
    # pythonic way
    def myPow1(self, x, n):
        import math
        return math.pow(x, n)
 
if __name__ == "__main__":
    ans = Solution()
    pow1 = ans.myPow1(2.1, 3)
    pow2 = ans.myPow2(2.1, 3) 
    pow3 = ans.myPow3(2.1, 3)
    if pow1 == pow2 and pow2 == pow3:
        print("pow test pass")
    else:
        print("my pow1 reutrn", ans.myPow1(2.1, 3)) 
        print("my pow2 reutrn:", ans.myPow2(2.1, 3)) 
        print("my pow3 reutrn:", ans.myPow3(2.1, 3)) 
        print("pow test failed") 
