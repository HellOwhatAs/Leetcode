#
# @lc app=leetcode.cn id=822 lang=python3
#
# [822] 翻转卡片游戏
#

# @lc code=start
from typing import List
from math import inf, isinf
class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        n, ret = len(fronts), inf
        for i in range(n):
            if_valid = ib_valid = True
            for j in range(n):
                if not (if_valid or ib_valid): break
                if i == j:
                    if fronts[i] == backs[j]:
                        if_valid = ib_valid = False
                else:
                    if not (fronts[i] != fronts[j] or fronts[i] != backs[j]):
                        if_valid = False
                    if not (backs[i] != fronts[j] or backs[i] != backs[j]):
                        ib_valid = False
            if if_valid: ret = min(ret, fronts[i])
            if ib_valid: ret = min(ret, backs[i])

        return 0 if isinf(ret) else ret
# @lc code=end

print(Solution().flipgame(fronts = [1,2,4,4,7], backs = [1,3,4,1,3]))
print(Solution().flipgame([1,1], [1,2]))