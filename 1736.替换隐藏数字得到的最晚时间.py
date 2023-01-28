#
# @lc app=leetcode.cn id=1736 lang=python3
#
# [1736] 替换隐藏数字得到的最晚时间
#

# @lc code=start
class Solution:
    def maximumTime(self, time: str) -> str:
        h, h1, _, m, m1 = time
        if h == '?': 
            if h1 in "456789": h = '1'
            else: h = '2'
        if h1 == '?':
            if h in '01': h1 = '9'
            else: h1 = '3'
        if m == '?': m = '5'
        if m1 == '?': m1 = '9'
        return f"{h}{h1}:{m}{m1}"
# @lc code=end

print(Solution().maximumTime("?4:03"))
