#
# @lc app=leetcode.cn id=85 lang=python3
#
# [85] 最大矩形
#

# @lc code=start
from typing import List
import numpy as np
class Solution:
    def largestRectangleArea(self,array:np.ndarray)->int:
        s,ret=[],0
        for i in range(array.shape[0]):
            while(s and array[s[-1]]>array[i]):
                tmp=s.pop()
                ret=max(ret,(i-s[-1]-1)*array[tmp])
            s.append(i)
        return ret
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:return 0
        matrix=(np.array(matrix)=="1").astype(np.int32)
        count=matrix[0].copy()
        for i in range(1,matrix.shape[0]):matrix[i]=count=count*matrix[i]+matrix[i]
        self.matrix=np.zeros((len(matrix),len(matrix[0])+2),dtype=np.int32)
        self.matrix[:,1:-1]=matrix
        ret=0
        for i in self.matrix:
            ret=max(ret,self.largestRectangleArea(i))
        return int(ret)

# @lc code=end
print(Solution().maximalRectangle([
    ["1","0","1","0","0"],
    ["1","0","1","1","1"],
    ["1","1","1","1","1"],
    ["1","0","0","1","0"]
]))