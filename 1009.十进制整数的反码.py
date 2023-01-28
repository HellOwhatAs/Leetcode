#
# @lc app=leetcode.cn id=1009 lang=python3
#
# [1009] 十进制整数的反码
#

# @lc code=start
from math import log2
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return ~n + 2**(int(log2(n))+1) if n>0 else 1
# @lc code=end

