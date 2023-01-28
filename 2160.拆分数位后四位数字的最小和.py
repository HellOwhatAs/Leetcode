#
# @lc app=leetcode.cn id=2160 lang=python3
#
# [2160] 拆分数位后四位数字的最小和
#

# @lc code=start
class Solution:
    def minimumSum(self, num: int) -> int:
        a, b, c, d = sorted(map(int, str(num)))
        return 10 * (a + b) + c + d
# @lc code=end

print(Solution().minimumSum(2932))