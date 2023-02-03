#
# @lc app=leetcode.cn id=2390 lang=python3
#
# [2390] 从字符串中移除星号
#

# @lc code=start
class Solution:
    def removeStars(self, s: str) -> str:
        ret = []
        for c in s:
            if c == '*': ret.pop()
            else: ret.append(c)
        return ''.join(ret)
# @lc code=end

