#
# @lc app=leetcode.cn id=2520 lang=python3
#
# [2520] 统计能整除数字的位数
#

# @lc code=start
from collections import Counter
class Solution:
    def countDigits(self, num: int) -> int:
        return sum(v for k, v in Counter(map(int, str(num))).items() if not num % k)
# @lc code=end

print(Solution().countDigits(1248))