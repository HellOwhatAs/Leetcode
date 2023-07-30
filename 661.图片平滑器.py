#
# @lc app=leetcode.cn id=661 lang=python3
#
# [661] 图片平滑器
#

# @lc code=start
from typing import List
import numpy as np
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        image = np.array(img)
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                img[i][j] = int(image[
                    max(0, i-1): min(i+2, image.shape[0]), 
                    max(0, j-1): min(j+2, image.shape[1])
                ].mean())
        return img
# @lc code=end

print(Solution().imageSmoother(img = [[1,1,1],[1,0,1],[1,1,1]]))
print(Solution().imageSmoother(img = [[100,200,100],[200,50,200],[100,200,100]]))