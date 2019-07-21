## Reference
# https://www.lintcode.com/problem/is-subsequence/description

## Medium - Pintrest - TwoPointers/String

## Description
# Given a string s and a string t, check if s is a subseqence of t.
# You may assume that there is only lower case English letters in both s and t.
# t is potentially a very long(length~=50,0000) string, and s is a short string(length < 100).

# A substring of a string is a new string which is formed from the original string by deleting some 
# (can be none) of the characters without disturbing the relative positions of the remaining characters.
# ie. "ace" is a subsequence of "abcde" while "aec" is not.

## Example
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Input: s = `"axc"`, t = `"ahbgdc"`
# Output: false

## Challenge
# If there are lots of incoming S1,S2....Sk where k>1B, and you want to check one by one to see 
# if T has its subsequence.
# In this senario, how would you change your code?

## Solution
class Solution(object):
    # KEY: 1) substring of string is a new string formed from the original by deleting some(can be none) characters.
    #      Therefore, "" is deleting all characters, so it's a substring of original
    # 2) O(N*M) => O(M): for i and for j and check subsequence; 
    #      Two pointers is a better one
    def isSubsequence(self, s, t):
        if not s:
            return True
        if not t:
            # in this case, s is non-empty
            return False
        N, M = len(s), len(t)
        if N > M:
            return False
        i, j = 0, 0
        while i < N and j < M:
            if s[i] == t[j]:
                i += 1
            j += 1
        if i < N:
            return False
        return True

if __name__ == "__main__":
    sol = Solution()
    s1, t1 = "", "abc"
    s2, t2 = "ab", "aecbace"
    s3, t3 = "ae", "acbd"

    print(sol.isSubsequence(s1,t1))
    print(sol.isSubsequence(s2,t2))
    print(sol.isSubsequence(s3,t3))

