#
# @lc app=leetcode.cn id=2119 lang=python3
#
# [2119] 反转两次的数字
#

# @lc code=start
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        while num:
            if not num % 10: return False
            num /= 10
        return True
# @lc code=end

for i in [526, 1800, 0]:
    print(Solution().isSameAfterReversals(i))