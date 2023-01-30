#
# @lc app=leetcode.cn id=1346 lang=python3
#
# [1346] 检查整数及其两倍数是否存在
#

# @lc code=start
from typing import List
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = set()
        for i in arr:
            if i * 2 in d or i % 2 == 0 and i // 2 in d: return True
            d.add(i)
        return False

# @lc code=end

