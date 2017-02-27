## Reference
# http://www.lintcode.com/en/problem/plus-one/

## Tags - Easy
# Array; Google

## Description
# Given a non-negative number represented as an array of digits, plus one to the number.
# The digits are stored such that the most significant digit is at the head of the list

## Analysis
# input - digits list 
# output - result list
# exception: empty list
# Steps:
#   no matter the number we need to add, we may have a more general solution
#   brute force
#   1) for simple problem, add a num smaller than 10
#      we only need to consider the solution that have one carrier
#      a. carerier flag to record the carrier from last digit
#      b. get the num and carrier by divide and mod
#      c. if reach the head, we need to append one more 

## Solution
class Solution:
    def plusGen(self, digits, num):
        if not digits or not num:
            return digits
        # init carrier to simplify the algorithm
        carrier = num
        N = len(digits)
        for i in xrange(N-1, -1, -1):
            digits[i] += carrier
            carrier = digits[i] // 10
            digits[i] %= 10
            # no matter i is 0 or not, when no carrier anymore, 
            # it should stop
            if not carrier:
                break
            # if carrier and i == 0, then we need insert 
            if i == 0:
                # insert carrier
                digits.insert(0, carrier)
        return digits 
 
    def plusOne(self, digits):
        num = 1
        return self.plusGen(digits, num)

if __name__ == "__main__":
    digits1, ans1 = [1, 2, 3], [1, 2, 4]
    digits2, ans2 = [9, 9, 9], [1, 0, 0, 0]
    ans = Solution()
    if ans.plusOne(digits1) == ans1 and ans.plusOne(digits2) == ans2:
        print("[passed] - Plus One test")
    else:
        print("[failed] - Plus One test")


