## Reference
# https://www.lintcode.com/problem/missing-number/description

## Medium - Greedy - Facebook/Microsoft/Bloomberg

## Description
# Given an array contains N numbers of 0 .. N, find which number doesn't exist in the array.
# 可以改变序列中数的位置。

## Example
# Input:[0,1,3]
# Output:2

# Input:[1,2,3]
# Output:0

# Challenge
# Do it in-place with O(1) extra memory and O(n) time.


## Solution
# progression: a series with a definite pattern of advance.
# 1. Math(arithmetic progression): total sum of 0..N is n * (a1+an)//2 => there are totally N+1 number, as 0 to N => (N+1)*(0+N)//2
# 2. XOR: bitwise Exclusive=> two same nums XOR => 0.  
# 3. Brute-force: set(), no ncessary on a hashmap
#


