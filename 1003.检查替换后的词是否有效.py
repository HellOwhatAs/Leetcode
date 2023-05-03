#
# @lc app=leetcode.cn id=1003 lang=python3
#
# [1003] 检查替换后的词是否有效
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        while True:
            s = s.replace('abc', '')
            if n == len(s): break
            n = len(s)
        return not s
# @lc code=end

