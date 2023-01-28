#
# @lc app=leetcode.cn id=2108 lang=python3
#
# [2108] 找出数组中的第一个回文字符串
#

# @lc code=start
from typing import List
class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            if i == i[::-1]:return i
        return ''
# @lc code=end

