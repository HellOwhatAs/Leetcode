#
# @lc app=leetcode.cn id=1446 lang=python3
#
# [1446] 连续字符
#

# @lc code=start
from itertools import groupby
class Solution:
    def maxPower(self, s: str) -> int:
        return max(len(list(it)) for c, it in groupby(s))
# @lc code=end

