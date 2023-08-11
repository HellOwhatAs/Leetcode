#
# @lc app=leetcode.cn id=1572 lang=python3
#
# [1572] 矩阵对角线元素的和
#

# @lc code=start
from typing import List
import numpy as np

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        matrix = np.array(mat)
        n = matrix.shape[0]
        return int(matrix[range(n), range(n)].sum() + 
            matrix[range(n), range(n-1, -1, -1)].sum() - 
            (matrix[(n-1)//2:n//2+1, (n-1)//2:n//2+1].sum() if n & 1 else 0)
        )
# @lc code=end

print(Solution().diagonalSum(mat = [
            [1,2,3],
            [4,5,6],
            [7,8,9]]))
print(Solution().diagonalSum(mat = [[1,1,1,1],
            [1,1,1,1],
            [1,1,1,1],
            [1,1,1,1]]))
print(Solution().diagonalSum(mat = [[5]]))