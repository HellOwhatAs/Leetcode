#
# @lc app=leetcode.cn id=2485 lang=python3
#
# [2485] 找出中枢整数
#

# @lc code=start
from math import sqrt
class Solution:
    def pivotInteger(self, n: int) -> int:
        x2 = (n + 1) * n // 2
        x = round(sqrt(x2))
        if x**2 == x2: return x
        return -1
# @lc code=end

print(Solution().pivotInteger(8))
print(Solution().pivotInteger(1))
print(Solution().pivotInteger(4))