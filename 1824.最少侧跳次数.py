#
# @lc app=leetcode.cn id=1824 lang=python3
#
# [1824] 最少侧跳次数
#

# @lc code=start
from typing import List
class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        data = [[float('inf')]*3 for _ in range(len(obstacles))]
        data[-1] = [0]*3
        for i in range(len(obstacles)-2, -1, -1):
            for j in range(3):
                if obstacles[i] != j+1 and obstacles[i+1] != j+1: data[i][j] =  min(data[i][j], data[i+1][j])
            for j in range(3):
                data[i][j] = min(data[i][j], min(data[i])+1)
        return data[0][1]

# @lc code=end
print(Solution().minSideJumps([0,2,1,0,3,0]))