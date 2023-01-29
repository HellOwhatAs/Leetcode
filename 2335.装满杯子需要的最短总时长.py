#
# @lc app=leetcode.cn id=2335 lang=python3
#
# [2335] 装满杯子需要的最短总时长
#

# @lc code=start
from typing import List
class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort()
        if amount[1] == 0: return amount[2]
        return self.fillCups([amount[0], amount[1] - 1, amount[2] - 1]) + 1
# @lc code=end

print(Solution().fillCups( [5,0,0]))