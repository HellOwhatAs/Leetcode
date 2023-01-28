#
# @lc app=leetcode.cn id=989 lang=python3
#
# [989] 数组形式的整数加法
#

# @lc code=start
from typing import List
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        return [int(i) for i in str(int("".join(str(j) for j in num))+k)]
# @lc code=end

