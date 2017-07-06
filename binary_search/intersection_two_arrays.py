## Reference
# http://www.lintcode.com/en/problem/intersection-of-two-arrays/
# 349 https://leetcode.com/problems/intersection-of-two-arrays/#/description

## Tags - Easy
# Binary Search; Two Pointers; Sort; Hash Table

## Description
# Given two arrays, write a function to compute their intersection.
# Notice: each element in the result MUST be unique; the result can be in ANY ORDER

## Challenge
# implement in three different algorithm

## Analysis
# input - two arrays; 
# output - intersections: unique items and not sorted 
# exception: empty or none - return []
# solutions:
#     hashtable
#     O(N) space O(N) time
#     1) two arrays - not sorted, 
#     

## Solution
class Solution:
    # python library - set
    # 1) list to set; 
    # 2) s.intersection(t)
    # 3) set to list
    def intersection1(self, nums1, nums2):
        if not nums1 or not nums2:
            return []
        result = []
        nums1 = set(nums1)
        nums2 = set(nums2)
        # sets operation returned sets !
        # so we have to convert it from set to list
        return list(nums2.intersection(nums1))

    def bsearch(self, array, target):
        if not array:
            return False
        N = len(array)
        start, end = 0, N-1
        while start+1 < end:
            middle = (start+end) // 2
            if array[middle] == target:
                return True
            if array[middle] < target:
                start = middle
            else:
                end = middle
        if array[start] == target or array[end] == target:
            return True
        return False 

    # Sort + binary search
    # O(MlogM+(M+N)logN) time; O(M+N) space
    def intersection2(self, nums1, nums2):
        # corner case can improve efficiency
        if not nums1 or not nums2:
            return []
        result = []
        nums1.sort()
        nums2.sort()
	M = len(nums2)
        for i in xrange(M):
            if i != 0 and nums2[i] == nums2[i-1]:
                continue
            if self.bsearch(nums1, nums2[i]):
                result.append(nums2[i])
        return result

    # hash table
    # O(M) + O(N) time; O(M)space
    def intersection3(self, nums1, nums2):
        if not nums1 or not nums2:
            return []
        result = []
        nums = {}
        # Traverse nums1
        for num in nums1:
            if num not in nums:
                nums[num] = 0
        for num in nums2:
            if num in nums:
                if nums[num] == 0:
                    result.append(num)
                    # KEY - facility to avoid the duplicates included into the result
                    nums[num] = 1
        return result  
       
    # sort and merge + hash
    # NlogN + N time; O(N)space 
    def intersection4(self, nums1, nums2):
        # corner case
        if not nums1 or not nums2:
            return []
        nums1.sort()
        nums2.sort()
        N, M = len(nums1), len(nums2)
        i, j = 0, 0
        result = {}
        while i < N and j < M:
            while i < N and j < M and nums1[i] < nums2[j]:
                i += 1
            while i < N and j < M and nums2[j] < nums1[i]:
                j += 1
            if i < N and j < M and nums1[i] == nums2[j]:
                if nums1[i] not in result:
                    result[nums1[i]] = True
                i += 1
                j += 1
        return result.keys()           
        
if __name__ == "__main__":
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    ans = Solution()
    if ans.intersection1(nums1, nums2) != [2] or \
        ans.intersection3(nums1, nums2) != [2] or \
        ans.intersection4(nums1, nums2) != [2] or \
        ans.intersection2(nums1, nums2) != [2]:
        print("Failed: intersection of two arrays")
    else:
        print("Passed: intersection of two arrays")
