#
# @lc app=leetcode.cn id=860 lang=python3
#
# [860] 柠檬水找零
#

# @lc code=start
from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        counts = [0, 0]
        for i in bills:
            if i == 5:
                counts[0] += 1
            elif i == 10:
                if counts[0] < 1: return False
                counts[0] -= 1
                counts[1] += 1
            else:
                if counts[1] >= 1 and counts[0] >= 1:
                    counts[0] -= 1
                    counts[1] -= 1
                elif counts[0] >= 3:
                    counts[0] -= 3
                else: return False
        return True
# @lc code=end

