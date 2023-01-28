#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start
from typing import List
class Solution:
    data={
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:return []
        ret=[""]
        for i in digits:ret=[j+k for k in self.data[i] for j in ret]
        return ret
# @lc code=end

