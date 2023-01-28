#
# @lc app=leetcode.cn id=1967 lang=python3
#
# [1967] 作为子字符串出现在单词中的字符串数目
#

# @lc code=start
from typing import List
class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(pattern in word for pattern in patterns)
# @lc code=end

