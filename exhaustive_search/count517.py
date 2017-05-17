#!/usr/bin/python2.7
# Author zwli
# combination +/-/*/// on input numbers, the target is 517.
# This a crack for china mobile activity 

import sys
class Solution:
	
    def counter(self, nums):
        if not nums:
	    return None
 	result = []
        visited = [False] * 4 
	self.helper(nums, 1, nums[0], visited, [], result)
        return result
    # permutation
    def helper(self, nums, sindex, target, visited, opes, result):
	#print(target)
        if target == 517:
            result.append(opes[:])
            return
         
        for i in xrange(sindex, len(nums)):
		
	    for j in xrange(4):
                if visited[j]:
		    continue
                visited[j] = True 
		if j == 0:
		    opes.append("+")
		    self.helper(nums, i+1, target+nums[i], visited, opes, result)
                elif j == 1:
		    opes.append("-")
		    self.helper(nums, i+1, target-nums[i], visited, opes, result)
		elif j == 2:
		    opes.append("x")   
		    self.helper(nums, i+1, target*nums[i], visited, opes, result)
		else:
		    opes.append("//")   
		    self.helper(nums, i+1, target//nums[i], visited, opes, result)
		opes.pop()
		visited[j] = False
	#print("Failed to find the result")
        #return

if __name__ == "__main__":
    nums = []
    for i in xrange(1, len(sys.argv)):
        nums.append(int(sys.argv[i]))	
    
    #nums = [20,20,25,3] 
    ans = Solution()
    print(ans.counter(nums))
