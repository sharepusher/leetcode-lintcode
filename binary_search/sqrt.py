## Reference
# http://www.lintcode.com/en/problem/sqrtx/
# 69 https://leetcode.com/problems/sqrtx/#/description

## Tags - Easy; Yellow
# Binary Search; Mathematics; Facebook

## Description
# Implement int sqrt(int x)
# Compute and return the square root of x

## Challenge
# O(log(X))

## Analysis
# Input - int X positive only? ; output - square root of X; 
# exception ? 0 return 0 or 1 return 1, if input negtive return None, as ONLY positive has square root
# steps: KEY - x is int, the num should be >= 0 and <= x, i.e. 0 <= num <= x
#        Find the LAST number that num**2(i.e. pow(num, 2)) <= x, in other words, num*num <= x
#        num can be treated as a sorted sequence, which start from 2 to x(maximum)
#   1) corner case: x is negtive; x == 0 or x== 1
#   2) init start_num from 2, end_num = x
#   3) check whether the middle is the target, if so, start = middle, drop the left half
#   4) if not, drop the right part, end = middle
# r*r = x, then r is the squar root of x.
# corner case: x should be positive
# 1) broute-force: increase r one by one, until the first r*r that greater than x
# and then we should return r-1,  but not r.
# 2) Newton
# 3) binary search: x is the largest r, so we can decrease to find the first r*r smaller than x.

## Solution
class Solution:
    # according to the defination of square root
    def sqrt3(self, x):
        ans = 0
        last_correct = 0
        while ans * ans <= x:
            last_correct = ans
            ans += 1
        return last_correct

    # improved binary search
    def sqrt2(self, x):
        if x is None or x < 0:
            return None
        if x in (0, 1):
            return x
        start, end = 1, x
        while start + 1 < end:
            middle = (start+end) // 2
            if middle ** 2 == x:
                return middle
            elif middle ** 2 > x:
                end = middle
            else:
                start = middle
        
        return start 

    # raw method based on the classical binary search
    # in fact, middle can be return directly if middle*middle == X,
    # in this case, the middle is what we are looking for. 
    def sqrt1(self, x):
        # corner case
        if x is None or x < 0:
            return None
        if x in (0, 1):
            return x
        # init
        # should start from 1 
        start, end = 1, x
        while start + 1 < end:
            middle = (start + end) // 2
            if middle ** 2 <= x:
                start = middle
            else:
                end = middle
        if end**2 <= x:
            return end
        if start**2 <= x:
            return start
        return None
    
    # python lib
    def sqrt4(self, x):
        if x < 0:
	    return None
        if x == 0 or x== 1:
	    return x
        import math
        # KEY: return int, but now float
        return int(math.sqrt(x))
 
if __name__ == "__main__":
    ans = Solution()
    if ans.sqrt1(1) == 1 and ans.sqrt2(1) == 1 and ans.sqrt3(1) == 1 \
        and ans.sqrt1(2) == 1 and ans.sqrt2(2) == 1 and ans.sqrt3(2) == 1 \
        and ans.sqrt1(3) == 1 and ans.sqrt3(3) == 1 and ans.sqrt3(3) == 1:
        print ("Passed: sqrt(x)")
    else:
        print("Failed: sqrt(x)")
