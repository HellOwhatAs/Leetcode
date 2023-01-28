#
# @lc app=leetcode.cn id=1957 lang=python3
#
# [1957] 删除字符使字符串变好
#

# @lc code=start
from itertools import groupby
class Solution:
    def makeFancyString(self, s: str) -> str:
        return "".join("".join(list(it)[:2]) for _, it in groupby(s))
# @lc code=end

print(Solution().makeFancyString("aaabaaaa"))