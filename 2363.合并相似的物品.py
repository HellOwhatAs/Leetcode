#
# @lc app=leetcode.cn id=2363 lang=python3
#
# [2363] 合并相似的物品
#

# @lc code=start
from typing import List
from collections import Counter
class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        return [[k, v] for k, v in sorted((Counter({k: v for k, v in items1}) + Counter({k: v for k, v in items2})).items(), key=lambda x:x[0])]
# @lc code=end

print(Solution().mergeSimilarItems(items1 = [[1,1],[4,5],[3,8]], items2 = [[3,1],[1,5]]))