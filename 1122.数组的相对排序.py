#
# @lc app=leetcode.cn id=1122 lang=python3
#
# [1122] 数组的相对排序
#

# @lc code=start
from typing import List
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        weight = {i:ii for ii,i in enumerate(arr2)}
        arr1.sort(key=lambda x:weight[x] if x in weight else len(arr2)+x)
        return arr1
# @lc code=end

