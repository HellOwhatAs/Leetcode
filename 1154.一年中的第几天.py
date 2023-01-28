#
# @lc app=leetcode.cn id=1154 lang=python3
#
# [1154] 一年中的第几天
#

# @lc code=start
from datetime import datetime
class Solution:
    def dayOfYear(self, date: str) -> int:
        return (datetime(int(date[:4]), int(date[5:7]), int(date[8:])) - datetime(int(date[:4]), 1, 1)).days + 1
# @lc code=end

print(Solution().dayOfYear("2019-02-10"))