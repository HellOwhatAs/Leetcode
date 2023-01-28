#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
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
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0],reverse=True)
        return self.func(intervals)
# @lc code=end
print(Solution().merge([[1,4],[0,2],[3,5]]))
