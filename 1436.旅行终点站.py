#
# @lc app=leetcode.cn id=1436 lang=python3
#
# [1436] 旅行终点站
#

# @lc code=start
from typing import List
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        return list(set(i[1] for i in paths) - set(i[0] for i in paths))[0]
# @lc code=end

print(Solution().destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))