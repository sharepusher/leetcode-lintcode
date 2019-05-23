## Two pointers
# 1. forward pointers
# 2. window(meet some condition): slow - fast
# https://www.lintcode.com/problem/longest-substring-without-repeating-characters/
# https://www.lintcode.com/problem/longest-substring-with-at-most-k-distinct-characters/description

# two layer iteration
# visited = {}
# result = some
# for left in range(N):
#     while right < N:
#         if meet_conditions:
#             visited[s[right]] = visited.get(s[right], 0) + 1 
#             right += 1
#         else:
#             break
#     # for substring problem, it can return when right == N
#     # as in this case, there's no larger substring than current.
#     if right == N:
#        
#         return result 
#     summary
#     update/remove s[left]
#              






