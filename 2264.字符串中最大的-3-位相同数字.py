#
# @lc app=leetcode.cn id=2264 lang=python3
#
# [2264] 字符串中最大的 3 位相同数字
#

# @lc code=start
from itertools import groupby
class Solution:
    def largestGoodInteger(self, num: str) -> str:
        return max(i if len(list(it)) >= 3 else '' for i, it in groupby(num)) * 3
# @lc code=end

print(Solution().largestGoodInteger("42352338"))