#
# @lc app=leetcode.cn id=1253 lang=python3
#
# [1253] 重构 2 行二进制矩阵
#

# @lc code=start
from typing import List
class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        ret = [[], []]
        for elem in colsum:
            if elem == 0: ret[0].append(0), ret[1].append(0)
            elif elem == 2:
                upper -= 1
                lower -= 1
                ret[0].append(1), ret[1].append(1)
            else:
                if upper > lower:
                    upper -= 1
                    ret[0].append(1), ret[1].append(0)
                else:
                    lower -= 1
                    ret[0].append(0), ret[1].append(1)
        if upper == lower == 0: return ret
        return []

# @lc code=end

print(Solution().reconstructMatrix(upper = 2, lower = 1, colsum = [1,1,1]))
print(Solution().reconstructMatrix(upper = 2, lower = 3, colsum = [2,2,1,1]))
print(Solution().reconstructMatrix(upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]))