#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#

# @lc code=start
from bisect import bisect_right
from typing import List
class Solution:
    def func(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)<2:return intervals
        if intervals[-1][1]>=intervals[-2][0]:
            tmp1=[intervals[-1][0],max(intervals[-1][1],intervals[-2][1])]
            intervals.pop()
            intervals.pop()
            intervals.append(tmp1)
            return self.func(intervals)
        tmp1=intervals.pop()
        tmp2=self.func(intervals)
        tmp2.append(tmp1)
        return tmp2
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.insert(bisect_right([i[0] for i in intervals],newInterval[0]),newInterval)
        intervals.reverse()
        return self.func(intervals)[::-1]
# @lc code=end

