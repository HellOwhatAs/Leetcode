#
# @lc app=leetcode.cn id=1620 lang=python3
#
# [1620] 网络信号最好的坐标
#

# @lc code=start
from typing import List
from itertools import product
class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        retval,ret=-float("inf"),None
        for x,y in product(range(51),range(51)):
            sig=0
            for i in towers:
                d=((i[0]-x)**2+(i[1]-y)**2)**0.5
                if d<=radius:
                    sig+=int(i[2]/(1+d))
            if sig>retval:
                retval=sig
                ret=[x,y]
        return ret
# @lc code=end

