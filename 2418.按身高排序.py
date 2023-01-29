#
# @lc app=leetcode.cn id=2418 lang=python3
#
# [2418] 按身高排序
#

# @lc code=start
from typing import List
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [i[0] for i in sorted(zip(names, heights), key=lambda x: -x[1])]
# @lc code=end

print(Solution().sortPeople(names = ["Alice","Bob","Bob"], heights = [155,185,150]))