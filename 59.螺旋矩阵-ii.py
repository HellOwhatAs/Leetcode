#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
from typing import List
def order_func(xl:int,yl:int):
    if not xl:return
    for i in range(xl):yield i,0
    if not yl-1:return
    for i in range(1,yl):yield xl-1,i
    if not xl-1:return
    for i in range(xl-2,-1,-1):yield i,yl-1
    if not yl-2:return
    for i in range(yl-2,0,-1):yield 0,i
    for x,y in order_func(xl-2,yl-2):yield x+1,y+1
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ret=[[0]*n for _ in range(n)]
        for i,(x,y) in enumerate(order_func(n,n)):
            ret[y][x]=i+1
        return ret
# @lc code=end

