## Reference leetcode455
# https://leetcode.com/problems/assign-cookies/#/description


## Tag - Easy
# Greedy; Two pointers


## Description
# Assume you are an awesome parent and want to give your children some cookies.
# But you should give each child at most one cookies.
# Each child i has a greed factor gi, which is the minimum size of a cookie that the child will be content with;
# and each cookie j has a size sj. If sj >= gi, we can assign the cookie j to the child i, and the child i will be content.
# Your goal is to maximize the number of your content children and output the maximum number.
# NOTE: you may assume the greed factor is always positive; you cannot assign more than one cookie to one child.
# Example1: Input [1, 2, 3] [1, 1] output - 1
# Example2: Input [1, 2] [1, 2, 3] output - 2

## Analysis
# Find the relationship between two list
# One child can only have one cookie at most, s[j] >= g[i]


## Solution
class Solution(object):
    def findContentChildren(self, g, s):
        if not g or not s:
            return 0   
        N, M = len(g), len(s)
        i, j = 0, 0
        # init result
        result = 0
        while i < N and j < M:
            if g[i] <= s[j]:
                result += 1
                i += 1
                j += 1
            else:
                j += 1
        return result

if __name__ == "__main__":
    g, s = [1, 2, 3], [1, 1] 
    ret = 1
    ans = Solution()
    if ret == ans.findContentChildren(g, s):
        print("Cookie passed.") 
    else:
        print("Cookie failed.")
