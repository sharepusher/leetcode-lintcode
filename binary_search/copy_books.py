## Reference
# https://www.lintcode.com/problem/copy-books/description
# https://blog.csdn.net/roufoo/article/details/87579774

## Hard - BinarySearch/Greedy/DP

## Description
# Given n books and the i-th book has pages[i] pages. 
# There are k persons to copy these books.
# These books list in a row and each person can claim a continous range of books.
# For example, one copier can copy the books from i-th to j-th continously,  
# but he can not copy the 1st book, 2nd book and 4th book (without 3rd book).
# They start copying books at the same time and they all cost 1 minute to copy 1 page of a book. 
# What's the best strategy to assign books so that the slowest copier can finish at earliest time?
# Return the shortest time that the slowest copier spends.

## Example
# Input: pages = [3, 2, 4], k = 2
# Output: 5
# Explanation: 
#     First person spends 5 minutes to copy book 1 and book 2.
#     Second person spends 4 minutes to copy book 3.

# Input: pages = [3, 2, 4], k = 3
# Output: 4
# Explanation: Each person copies one of the books.

## Challenge
# O(nk) time

## Analysis
# What's the best strategy to assign books so that the slowest copier can finish at earliest time? => Typical find the smallest maximum problem
# shortest time that the slowest copier spends => the spend_time(Tm) is the target
# What's the Tm range? if 1 persion copy all the book, the Tm is sum(pages), then it's the maximum_tm, 
# as in this case, it has to copy each page all by one person.
# The max(pages) is the smallest time the worker has to spend, as all the book cannot split or separated
# Then the Tm should be among max(pages) and sum(pages)
# find the first target that meet the requirement 

## Solution







