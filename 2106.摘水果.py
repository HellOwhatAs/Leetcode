#
# @lc app=leetcode.cn id=2106 lang=python3
#
# [2106] 摘水果
#

# @lc code=start
from typing import List
class Solution:
    @staticmethod
    def step(left: int, right: int, fruits: List[List[int]], startPos: int) -> int:
        if fruits[right][0] <= startPos: return startPos - fruits[left][0]
        elif fruits[left][0] >= startPos: return fruits[right][0] - startPos
        else: return min(abs(startPos - fruits[right][0]), abs(startPos - fruits[left][0])) + fruits[right][0] - fruits[left][0]
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        left, right, sum, ans, n = 0, 0, 0, 0, len(fruits)
        while right < n:
            sum += fruits[right][1]
            while left <= right and self.step(left, right, fruits, startPos) > k:
                sum -= fruits[left][1]
                left += 1
            ans = max(ans, sum)
            right += 1
        return ans
# @lc code=end

