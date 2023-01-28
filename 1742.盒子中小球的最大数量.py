#
# @lc app=leetcode.cn id=1742 lang=python3
#
# [1742] 盒子中小球的最大数量
#

# @lc code=start
from collections import defaultdict
class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        d=defaultdict(int)
        for i in range(lowLimit,highLimit+1):
            d[sum(int(j) for j in str(i))]+=1
        return max(d.values())
# @lc code=end

