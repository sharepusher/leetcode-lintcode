## Reference
# https://leetcode.com/problems/valid-anagram/#/description
# http://www.lintcode.com/en/problem/two-strings-are-anagrams/#



## Tags - Easy
# String; Cracking The Coding Interview



## Two Strings Are Anagrams
# Write an interface anagram(s,t) to decide if two strings are anagrams or not.
# Clarification:
# What is Anagram?
# Two strings are anagram if they can be the same after change the order of characters.
# Example:
# 1) s = 'abcd', t = 'cbad', return True;
# 2) s = 'ad', t = 'ad', return True;
# 3) s = 'a', t = 'b', return false;


## Challenge:
# O(N) time; O(1) extra space


## Analysis
# input - string s and t
# output - True if anagram or False if not
# 1) the length of s and t should be the same
# 2) they are string, immutable; so we have to use sorted, or change str to list 
# 3) collections.Counter() 


## Solutions
from collections import Counter
class Solution:
    # Collections.Counter: O(N) time; O(N) space
    def anagram3(self, s, t):
        if not s and not t:
            return True
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)      

    # sort: O(NlogN) time; O(N) space
    def anagram2(self, s, t):
        if not s and not t:
            return True
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

    # hashmap: O(N) time; O(N) space
    def anagram1(self, s, t):
        if not s and not t:
            return True
        if len(s) != len(t):
            return False
        hmap = {} 
        for char in s:
            if char in hmap:
                hmap[char] += 1
            else:
                hmap[char] = 1
        for char in t:
            if char in hmap:
                if hmap[char]:
                    hmap[char] -= 1
                else:
                    return False
            else:
                return False
        return True

if __name__ == "__main__":
    s1, t1, ans1 = "abcd", "dcab", True
    s2, t2, ans2 = "", "", True
    s3, t3, ans3 = "", "a", False
    s4, t4, ans4 = "ab", "ac", False
    ans = Solution()
    if ans.anagram1(s1, t1) == ans1 and ans.anagram2(s1, t1) == ans1 and ans.anagram3(s1, t1) == ans1 and \
    ans.anagram1(s2, t2) == ans2 and ans.anagram2(s2, t2) == ans2 and ans.anagram3(s2, t2) == ans2 and \
    ans.anagram1(s2, t2) == ans2 and ans.anagram2(s2, t2) == ans2 and ans.anagram3(s2, t2) == ans2 and \
    ans.anagram1(s3, t3) == ans3 and ans.anagram2(s3, t3) == ans3 and ans.anagram3(s3, t3) == ans3 and \
    ans.anagram1(s3, t3) == ans3 and ans.anagram2(s3, t3) == ans3 and ans.anagram3(s3, t3) == ans3 and \
    ans.anagram1(s4, t4) == ans4 and ans.anagram2(s4, t4) == ans4 and ans.anagram3(s4, t4) == ans4 and \
    ans.anagram1(s4, t4) == ans4 and ans.anagram2(s4, t4) == ans4 and ans.anagram3(s4, t4) == ans4:
        print("Passed: valid anagram.") 
    else:
        print("Failed: valid anagram.")

 

