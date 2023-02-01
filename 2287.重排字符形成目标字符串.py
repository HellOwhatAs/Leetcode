#
# @lc app=leetcode.cn id=2287 lang=python3
#
# [2287] 重排字符形成目标字符串
#

# @lc code=start
from collections import Counter
from time import sleep
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        c, t = Counter(s), Counter(target)
        return min(c[k] // t[k] for k in t)
# @lc code=end

print(Solution().rearrangeCharacters(s = "ilovecodingonleetcode", target = "code"))