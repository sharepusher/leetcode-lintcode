## Reference 
# https://www.lintcode.com/problem/first-bad-version/description

## Medium - Facebook

## Description
# The code base version is an integer start from 1 to n. One day, someone committed a bad version in the code case, 
# so it caused this version and the following versions are all failed in the unit tests. Find the first bad version.
# You can call isBadVersion to help you determine which version is the first bad one. The details interface can be found in the code's annotation part.

## Example
# Given n = 5:

#  isBadVersion(3) -> false
#  isBadVersion(5) -> true
#  isBadVersion(4) -> true

# Here we are 100% sure that the 4th version is the first bad version.

## Challenge
# You should call isBadVersion as few as possible.


## Anaylysis


#class SVNRepo:
#    @classmethod
#    def isBadVersion(cls, id)
#        # Run unit tests to check whether verison `id` is a bad version
#        # return true if unit tests passed else false.
# You can use SVNRepo.isBadVersion(10) to check whether version 10 is a 
# bad version.

class Solution:
    """
    @param n: An integer
    @return: An integer which is the first bad version.
    """
    # The first position of the target
    # corner case, what if there's no bad version ?
    # There must be a bad version?
    def findFirstBadVersion(self, n):
        pass
