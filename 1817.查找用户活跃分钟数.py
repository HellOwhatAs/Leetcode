#
# @lc app=leetcode.cn id=1817 lang=python3
#
# [1817] 查找用户活跃分钟数
#

# @lc code=start
from typing import List
from collections import defaultdict
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        ret, d = [0]*k, defaultdict(set)
        for ID, t in logs: d[ID].add(t)
        for ID in d: ret[len(d[ID])-1] += 1
        return ret
# @lc code=end

