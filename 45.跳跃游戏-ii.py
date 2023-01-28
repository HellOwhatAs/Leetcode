#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#

# @lc code=start
from typing import List
class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        到达ind的最小步数=[n+1]*n
        到达ind的最小步数[0]=0
        for i in range(n-1):
            for j in range(nums[i]):
                if i+j+1<n:
                    到达ind的最小步数[i+j+1]=min(到达ind的最小步数[i+j+1],到达ind的最小步数[i]+1)
        return 到达ind的最小步数[-1]
# @lc code=end