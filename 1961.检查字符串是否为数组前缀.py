#
# @lc app=leetcode.cn id=1961 lang=python3
#
# [1961] 检查字符串是否为数组前缀
#

# @lc code=start
from typing import List
class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        start = 0
        for word in words:
            if s.startswith(word, start):
                start += len(word)
                if start == len(s): return True
            else:
                return False
        return start == len(s)
# @lc code=end

