#
# @lc app=leetcode.cn id=2169 lang=python3
#
# [2169] 得到 0 的操作数
#

# @lc code=start
class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        ret = 0
        while not (num1 == 0 or num2 == 0):
            if num1 >= num2:
                num1 -= num2
            else:
                num2 -= num1
            ret += 1
        return ret
# @lc code=end

print(Solution().countOperations(num1 = 10, num2 = 10))