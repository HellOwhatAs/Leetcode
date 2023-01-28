#
# @lc app=leetcode.cn id=1408 lang=python3
#
# [1408] 数组中的字符串匹配
#

# @lc code=start
from typing import List
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ret = []
        for i in words:
            for j in words:
                if i != j and i in j:
                    ret.append(i)
                    break
        return ret
# @lc code=end

