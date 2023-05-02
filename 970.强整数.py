#
# @lc app=leetcode.cn id=970 lang=python3
#
# [970] 强整数
#

# @lc code=start
from typing import List
from math import log, ceil
from itertools import product
class Solution:
    powerfulIntegers = lambda self, x, y, bound: list({tmp for i, j in product(range((ceil(log(bound, x)) if x != 1 else 0) + 1), range((ceil(log(bound, y)) if y != 1 else 0) + 1)) if (tmp := x ** i + y ** j) <= bound}) if bound != 0 else []
# @lc code=end

print(Solution().powerfulIntegers(x = 2, y = 3, bound = 10))
print(Solution().powerfulIntegers(x = 3, y = 5, bound = 15))
print(Solution().powerfulIntegers(2, 1, 10))
print(Solution().powerfulIntegers(2, 3, 0))