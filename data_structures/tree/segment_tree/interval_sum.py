## Reference
# http://www.lintcode.com/en/problem/interval-sum/#

## Tags - Medium
# Binary Search, Segment Tree

## Challenge
# O(logN) time for each query

## Description
# Given an integer array (index from 0 to n-1, where n is the size of this array)
# and an query list.
# Each query has two integers [start, end].
# For each query, calculate the sum number betwen index start and end in the given array, 
# return the result list.
# For array [1, 2, 7, 8, 5], and queries[(0,4), (1, 2), (2, 4)], return [23, 9, 20]

## Analysis
# input - the array and queries; output - list of sums of queries
# for interval related problem, we can use segment tree.
# The build process cost O(N) time and O(2^N) space, for we have to setup 2^N-1 nodes for the entire tree
# but the height of the tree is log(N)
# therefore, the query and modify cost log(N)
# the other method is the presum by DP, which also cost O(N) space and time to setup and modify, but only O(1) to query.

## Solution
# definition of interval objects
class Interval(object):
    def __init__(self, start, end):
        self.start, self.end = start, end

# definition of segment sum tree
class SegmentTree:
    def __init__(self, start, end, isum):
        self.start, self.end, self.isum = start, end, isum
        self.left, self.right = None, None
    
    # build interface of segment tree
    # @params: array, and index
    # @return: the root of the bult segment tree
    @classmethod
    def build(cls, A, start, end):
        if not A:
            return None
        root = SegmentTree(start, end, A[start])
        # base case
        if start == end:
            return root
        # now start!=end, go to left and right
        left = cls.build(start, (start+end)//2)
        right = cls.build((start+end)//2+1, end)
        root.left, root.right = left, right
        root.isum = left.isum+right.isum
        return root
    # query interface
    # @params: the root of the segment tree is the basic!
    # @return: the sum of the interval
    # the key of the query is that find the out of range; in the range; cross the range return
    @classmethod
    def query(cls, root, start, end):
        # corner case
        if not root:
            return None
        # out of range
        if root.start > end or root.end < start:
            # As we are calculating the sum, the invalid should NOT impact the valid
            # we have to merge left and right by sum, so 0 is the best return.
            return 0
        # in the range
        if root.start >= start and root.end <= end:
            return root.isum
        # cross the range
        left = cls.query(root.left, start, end)
        right = cls.query(root.right, start, end)
        return left+right

class Solution:
    # segment tree
    def intervalSum1(self, A, queries):
        # corner case
        if not A or not queries
            return []
        result = []
        # build the segment tree first
        root = SegmentTree.build(A, 0, len(A)-1)       
            
        for query in queries:
            result.append(SegmentTree.query(root, query.start, query.end))
        return result

    # DP - presum
    def intervalSum2(self, A, queries):
        # corner case 
        if not A or not queries:
            return []
        result = []
        # presum
        N = len(A)
        presum = [0] * N
        # init the state first
        presum[0] = A[0]
        for i in xrange(1, N):
            presum[i] = presum[i-1] + A[i]
        # query process
        for query in queries:
            result.append(presum[query.end]-presum[query.start]+A[start])
        return result
   
