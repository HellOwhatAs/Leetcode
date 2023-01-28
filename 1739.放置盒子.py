#
# @lc app=leetcode.cn id=1739 lang=python3
#
# [1739] 放置盒子
#

# @lc code=start
from math import ceil,sqrt
class Solution:
    def minimumBoxes(self, n: int) -> int:
        i=int(pow(6*n, 1/3))
        if i*(i+1)*(i+2)//6<n:i+=1
        n-=(i-1)*i*(i+1)//6
        j=ceil((sqrt(8*n+1)-1)/2)
        return (i-1)*i//2+j
# @lc code=end
