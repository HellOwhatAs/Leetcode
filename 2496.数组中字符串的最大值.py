#
# @lc app=leetcode.cn id=2496 lang=python3
#
# [2496] 数组中字符串的最大值
#

# @lc code=start
from typing import List
class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        return max(int(i) if i.isdigit() else len(i) for i in strs)
# @lc code=end

