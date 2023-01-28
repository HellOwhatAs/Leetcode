#
# @lc app=leetcode.cn id=541 lang=python3
#
# [541] 反转字符串 II
#

# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        return "".join(s[i:i+k] if ii%2 else s[i:i+k][::-1] for ii, i in enumerate(range(0, len(s), k)))
# @lc code=end

print(Solution().reverseStr(s = "abcd", k = 2))