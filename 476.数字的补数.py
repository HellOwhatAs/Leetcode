#
# @lc app=leetcode.cn id=476 lang=python3
#
# [476] 数字的补数
#

# @lc code=start
from math import log2
class Solution:
    def findComplement(self, num: int) -> int:
        return ~num + 2**(int(log2(num))+1)
# @lc code=end

