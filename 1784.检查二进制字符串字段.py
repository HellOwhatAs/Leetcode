#
# @lc app=leetcode.cn id=1784 lang=python3
#
# [1784] 检查二进制字符串字段
#

# @lc code=start
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return len([i for i in s.split('0') if i])<=1
# @lc code=end

print(Solution().checkOnesSegment("1101"))