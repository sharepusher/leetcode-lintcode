## Reference
# http://www.lintcode.com/en/problem/intersection-of-two-arrays/

## Tags
# Easy - Binary Search; Two Pointers; Sort; Hash Table

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
    def intersection1(self, nums1, nums2):
        if not nums1 or not nums2:
            return []
        result = []
        nums1 = set(nums1)
        nums2 = set(nums2)
        # sets operation returned sets !!!
        # so we have to convert it from set to list
        return list(nums2.intersection(nums1))

    def binarySearch(array, target):
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
        if array[start] == target:
            return True
        if array[end] == target:
            return True
        return False 

    # bninary search
    # O(MlogM+NlogN) time; O(M+N) time
    def intersection2(self, nums1, nums2):
        if not nums1 or not nums2:
            return []
        # init result
        result = []
        # sort first ?
        nums1.sort()
        nums2.sort()
        robot = 0
        N = len(nums2)
        while robot < N:
            if robot + 1 < N and nums2[robot]
        
         
       


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
                    nums[num] = 1
        return result  
                 
        
if __name__ == "__main__":
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    ans = Solution()
    if ans.intersection1(nums1, nums2) != [2] or \
        ans.intersection3(nums1, nums2) != [2]:
        print("test failed")
    else:
        print("test passed")
