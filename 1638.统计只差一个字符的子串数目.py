#
# @lc app=leetcode.cn id=1638 lang=python3
#
# [1638] 统计只差一个字符的子串数目
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        ret = 0
        for i in range(len(s)):
            for j in range(len(t)):
                diff = 0
                for k in range(min(len(s) - i, len(t) - j)):
                    diff += s[i + k] != t[j + k]
                    ret += diff == 1
                    if diff > 1: break
        return ret
# @lc code=end

print(Solution().countSubstrings(s = "aba", t = "baba"))
print(Solution().countSubstrings(s = "ab", t = "bb"))