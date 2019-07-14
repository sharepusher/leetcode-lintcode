## Reference
# https://www.lintcode.com/problem/chalkboard-xor-game/description

## Medium - GameTheory/Mathematics - Garena

## Description
# We are given non-negative integers nums[i] which are written on a chalkboard. 
# Alice and Bob take turns erasing exactly one number from the chalkboard, with Alice starting first.
# If erasing a number causes the bitwise XOR of all the elements of the chalkboard to become 0, then that player loses.
# (Also, we'll say the bitwise XOR of one element is that element itself, and the bitwise XOR of no elements is 0.)
# Also, if any player starts their turn with the bitwise XOR of all the elements of the chalkboard equal to 0, then that player wins.
# Determine if Alice has a winning stargety, assuming both players play optimally.
# 1 <= nums.length <= 1000
# 0 <= nums[i] <= 2^16

## Example
# Input: [1, 1, 2]
# Output: false
# Explanation: 
#   Alice has two choices: erase 1 or erase 2.
#   If she erases 1, the nums array becomes [1, 2]. 
#   The bitwise XOR of all the elements of the chalkboard is 1 XOR 2 = 3. 
#   Now Bob can remove any element he wants, because Alice will be the one to erase the last element and she will lose. 
#   If Alice erases 2 first, now nums becomes [1, 1]. The bitwise XOR of all the elements of the chalkboard is 1 XOR 1 = 0. Alice will lose.
#
# Input: [1, 1, 1, 2]
# Output: true
# Explanation: Alice can erase 2 and the array becomes [1, 1, 1]. After Bob's erasure, the array becomes [1, 1] and 1 XOR 1 = 0.

## Analysis
# 1) Alice will win directly if the nums XOR is 0 OR there's no value in the empty nums.
# 2) When the nums XOR is not 0
#    Then whether Alice win or lose depends on the number of the array
#    if the num of array is even, then Alice will win; or Alice will lose.
# Explanation:
#    Define the min XOR subarray: the XOR of the subarray is 0; when remove any of them, the XOR won't be 0;
#    1) Assume the entire array is composed by some XOR subarray X1,X2 .. Xn, and the other are the independent numbers B1, B2 ...Bm
#    2) Both of them are optimally, therefore, both of them will try their best to win.
#    3) Therefore, no matter who is in turn to erase the number, they will use the best strategy:
#    4) In other words, if the total XOR is non-zero, and the number of independent numbers is greater than 1, then they will erase anyone from it.
#    5) If there's only 1 independent number left, they will choose from any XOR subarray and make the XOR sub-array
#       in this case, the XOR subarray and independent numbers will be counted again, as they may change.
#    6) Therefore, they can fight until the last number, in that case, they will or lose depends on the number of the total array.
#       If the number is even, then Alice win, or Bob win.



