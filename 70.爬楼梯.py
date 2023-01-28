#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
from functools import lru_cache
class Solution:
    @lru_cache
    def climbStairs(self, n: int) -> int:
        if n<3:return n
        return self.climbStairs(n-1)+self.climbStairs(n-2)
# @lc code=end

print(Solution().climbStairs(3))