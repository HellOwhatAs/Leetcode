#
# @lc app=leetcode.cn id=1163 lang=python3
#
# [1163] 按字典序排在最后的子串
#

# @lc code=start
class Solution:
    def lastSubstring(self, s: str) -> str:
        return max(s[i:] for i in range(len(s)))
# @lc code=end

