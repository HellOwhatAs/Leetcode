#
# @lc app=leetcode.cn id=1342 lang=python3
#
# [1342] 将数字变成 0 的操作次数
#

# @lc code=start
class Solution:
    def numberOfSteps(self, num: int) -> int:
        ret = 0
        while num:
            if num % 2: num -= 1
            else: num //= 2
            ret += 1
        return ret
# @lc code=end
