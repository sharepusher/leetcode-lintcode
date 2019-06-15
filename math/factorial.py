## Reference
# https://www.lintcode.com/problem/factorial/description

## Mathematics

## Descrption
# Given a number n, return the factorial of the number as a string

## Example
# Input: 0
# Output: "1"

# Input: 20
# Output: "2432902008176640000"

## Analysis
# 1. n should be positive integer
# 2. the factorial of num should be multiple of 1 to N.
# 3. N! = N*(N-1)!
# 4. 0! is 1.

## Solution
class Solution(object):
    def factorial(self, n):
        if n == 0 or n == 1:
            return "1"
        result = 1
        for i in xrange(2, n+1):
            result *= i
        return str(result)
    
    def factorial2(self, n):
        if n == 0 or n == 1:
            return "1"
        return str(self.helper(n))
    def helper(self, n):
        if n == 1:
            return 1
        return self.helper(n-1)*n

if __name__ == "__main__":
    ans = Solution()
    if ans.factorial(20) == ans.factorial2(20):
        print("pass")
    else:
        print("fail")




