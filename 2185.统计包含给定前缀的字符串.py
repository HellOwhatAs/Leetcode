#
# @lc app=leetcode.cn id=2185 lang=python3
#
# [2185] 统计包含给定前缀的字符串
#

# @lc code=start
from typing import List
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(i.startswith(pref) for i in words)
# @lc code=end

