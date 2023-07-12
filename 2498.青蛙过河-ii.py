#
# @lc app=leetcode.cn id=2498 lang=python3
#
# [2498] 青蛙过河 II
#

# @lc code=start
from typing import List
class Solution:
    @staticmethod
    def max_diff(a: List[int]):
        return max((a[i] - a[i - 1] for i in range(1, len(a))), default=0)
    def maxJump(self, stones: List[int]) -> int:
        return max(self.max_diff(stones[::2]), self.max_diff(stones[1::2]), stones[-1] - stones[-2], stones[1])
# @lc code=end

print(Solution().maxJump(stones = [0,2,5,6,7]))
print(Solution().maxJump(stones = [0,3,9]))