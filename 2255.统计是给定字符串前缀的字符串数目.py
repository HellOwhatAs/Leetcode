#
# @lc app=leetcode.cn id=2255 lang=python3
#
# [2255] 统计是给定字符串前缀的字符串数目
#

# @lc code=start
from typing import List
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        return sum(s.startswith(word) for word in words)
# @lc code=end

