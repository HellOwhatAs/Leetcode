#
# @lc app=leetcode.cn id=119 lang=python3
#
# [119] 杨辉三角 II
#

# @lc code=start
from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        ret=[1]
        for i in range(rowIndex):
            ret=[ret[0]]+[ret[i-1]+ret[i] for i in range(1,len(ret))]+[ret[-1]]
        return ret
# @lc code=end

