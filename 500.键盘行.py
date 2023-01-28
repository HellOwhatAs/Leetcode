#
# @lc app=leetcode.cn id=500 lang=python3
#
# [500] 键盘行
#

# @lc code=start
from typing import List
class Solution:
    line1, line2, line3 = set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")
    @staticmethod
    def valid(word: str) -> bool:
        word = word.lower()
        l = Solution.line1 if word[0] in Solution.line1 else \
            Solution.line2 if word[0] in Solution.line2 else \
            Solution.line3
        for c in word[1:]:
            if not c in l: return False
        return True
    def findWords(self, words: List[str]) -> List[str]:
        return [word for word in words if self.valid(word)]
# @lc code=end

