#
# @lc app=leetcode.cn id=1237 lang=python3
#
# [1237] 找出给定方程的正整数解
#
class CustomFunction:
    # Returns f(x, y) for any given positive integers x and y.
    # Note that f(x, y) is increasing with respect to both x and y.
    # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
    def f(self, x, y):
        return x + y

# @lc code=start
from typing import List
from bisect import bisect_left
"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""
class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ret, x, tmp = [], 1000, range(1001)
        for y in range(1, 1001):
            x = bisect_left(tmp, z, 1, x, key = lambda x: customfunction.f(x, y))
            if customfunction.f(x, y) == z:
                ret.append([x, y])
        return ret
# @lc code=end

print(Solution().findSolution(CustomFunction(), 5))