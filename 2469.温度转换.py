#
# @lc app=leetcode.cn id=2469 lang=python3
#
# [2469] 温度转换
#

# @lc code=start
from typing import List
class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        return [celsius + 273.15, celsius * 1.80 + 32.00]
# @lc code=end

