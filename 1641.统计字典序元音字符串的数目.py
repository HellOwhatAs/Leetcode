#
# @lc app=leetcode.cn id=1641 lang=python3
#
# [1641] 统计字典序元音字符串的数目
#

# @lc code=start
from math import comb
class Solution:
    def countVowelStrings(self, n: int) -> int:
        return comb(n + 4, 4)
# @lc code=end

print(Solution().countVowelStrings(1))