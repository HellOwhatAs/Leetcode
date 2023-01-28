#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
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
from typing import List,Tuple
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return [matrix[y][x] for x,y in order_func(len(matrix[0]),len(matrix))]

# @lc code=end

"""
m * n
---
r->n
d->m-1
l->n-1
u->m-2
"""