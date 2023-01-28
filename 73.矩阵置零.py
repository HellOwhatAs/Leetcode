#
# @lc app=leetcode.cn id=73 lang=python3
#
# [73] 矩阵置零
#

# @lc code=start
from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n=len(matrix),len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:matrix[i][j]=None
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==None:
                    for k in range(m):
                        if matrix[k][j]!=None:matrix[k][j]=0
                    for k in range(n):
                        if matrix[i][k]!=None:matrix[i][k]=0
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==None:matrix[i][j]=0
# @lc code=end

