## Reference
# http://www.lintcode.com/en/problem/hash-function/

## Tags - Easy
# Hash Table

## Description
# In data structure hash, hash function is used to convert a string (or any other type)
# into an integer smaller than hash size and bigger or equal to zero.
# The objective of designing a hash function is to "hash" the keys as unreasonable as possible.
# A good hash function can avoid collision as less as possible.
# A widely used hash function algorithm is using a magic number 33, consider any string as a 33 based 
# big integer like follow:
# hashcode("abcd") = (ascii(a)*33^3 + ascii(b)*33^2+ascii(c)*33+ascii(d)) % HASH_SIZE
#   = (97*33^3 + 98*33^2 + 77*33 + 100) % HASH_SIZE
# here HASH_SIZE is the capacity of the hash table(you can assume a hash table is like an array with index 0~HASH_SIZE-1).
# Given a string as a key and the size of hash table, return the hash value of this key.
## Clarification
# For this problem, you are not necessary to design your own hash algorithm or consider any collision issue, you just need to 
# implement the algorithm as described.
# Example: For key= "abcd", and size=1000, return 78.

## Analysis
# base 33 => ord: convert ONE character to ascii number
#  ans = (ans*33 + ord(x))

## Solution
class Solution:
    def hashCode(self, key, HASH_SIZE):
        ans = 0
        # whenever one character more, the 33 will be increased
        for x in key:
            ans = (ans*33 + ord(x)) % HASH_SIZE
    return ans

if __name__ == "__main__":
    ans = Solution()
    key = "abcd"
    size = 100
    if 78 == ans.hashCode(key, size):
        print("Passed: Hash Function.")
    else:
        print("Failed: Hash Function.") 


