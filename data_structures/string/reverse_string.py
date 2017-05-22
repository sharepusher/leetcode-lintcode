## Reference
# https://leetcode.com/problems/reverse-string/#/description

## Tags - Easy
# Two pointers; Divde and conquer; String;
  
## Description
# Write a function that takes a string as input and returns the string reversed.
# Example:
# Given s = "hello", return "olleh".

## Analysis
# 1) pythonic slice reverse
# 2) reverse xrange traverse
# 3) index decrease traverse
# 4) two pointers and merge list
# 5) divide and conquer

## Solutions
class Solutions(object):
    # pythonic
    def reverseString1(self, s):
        if not s:
	    return s
	return s[::-1]

    # reverse traverse
    def reverseString2(self, s):
	if not s:
	    return s
	N = len(s)
 	result = ""
	for i in xrange(N-1, -1, -1):
	    result += s[i]
	return result

    # two pointer
    def reverseString3(self, s):
	if not s:
	    return s
	N = len(s)
        result = [""] * N
	start, end = 0, N-1
	while start <= end:
	    result[start], result[end] = s[end], s[start]
	    start += 1
            end -= 1
	return "".join(result)
    
    # divide and conquer
    def reverseString4(self, s):
	if not s:
	    return s
	start, end = 0, len(s)-1
	return self.helper(s, start, end)
    def helper(self, s, start, end):
	if start == end:
	    return s[start]
	middle = (start+end) >> 1
	left = self.helper(s, start, middle) 
        right = self.helper(s, middle+1, end)
	return right + left

if __name__ == "__main__":
    s = "hello"
    target = "olleh"
    ans = Solutions()
    if ans.reverseString1(s) == target and ans.reverseString2(s)==target and \
    ans.reverseString3(s) == target and ans.reverseString4(s) == target:
	print("Passed: reverse String.")
    else:
	print("Failed: reverse String.")



