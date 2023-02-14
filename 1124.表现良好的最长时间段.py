#
# @lc app=leetcode.cn id=1124 lang=python3
#
# [1124] 表现良好的最长时间段
#

# @lc code=start
from typing import List
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        n = len(hours)
        s = [0] * (n + 1)
        stk = [0]
        for i in range(1, n + 1):
            s[i] = s[i - 1] + (1 if hours[i - 1] > 8 else -1)
            if (s[stk[-1]] > s[i]):
                stk.append(i)

        res = 0
        for r in reversed(range(1, n + 1)):
            while (stk and s[stk[-1]] < s[r]):
                res = max(res, r - stk.pop())
        return res
# @lc code=end
print(Solution().longestWPI([6,6,9]))
print(Solution().longestWPI([9,9,6,0,6,6,9]))
print(Solution().longestWPI([6,6,6]))

'''
-1, -1,  1
 0, -1, -2
'''