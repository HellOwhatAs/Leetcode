#
# @lc app=leetcode.cn id=1876 lang=python3
#
# [1876] 长度为三且各字符不同的子字符串
#

# @lc code=start
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ret = 0
        for i in range(2, len(s)):
            if s[i-2] != s[i-1] and s[i] != s[i-1] and s[i] != s[i-2]:
                ret += 1
        return ret
# @lc code=end

