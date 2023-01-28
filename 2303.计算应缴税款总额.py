#
# @lc app=leetcode.cn id=2303 lang=python3
#
# [2303] 计算应缴税款总额
#

# @lc code=start
from typing import List
class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        ret  = 0
        for i in range(len(brackets)):
            if brackets[i][0] > income:
                ret += (income - (brackets[i-1][0] if i-1 >= 0 else 0)) * brackets[i][1]
                break
            else:
                ret += (brackets[i][0] - (brackets[i-1][0] if i-1 >= 0 else 0)) * brackets[i][1]
        return ret/100
# @lc code=end

print(Solution().calculateTax(brackets = [[2,50]], income = 0))