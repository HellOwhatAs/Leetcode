#
# @lc app=leetcode.cn id=1925 lang=python3
#
# [1925] 统计平方和三元组的数目
#

# @lc code=start
from itertools import product
from math import sqrt
class Solution:
    def countTriples(self, n: int) -> int:
        ret = 0
        for a, b in product(range(1, n + 1), range(1, n + 1)):
            tmp = a ** 2 + b ** 2
            c = int(sqrt(tmp))
            if 1 <= c <= n and c ** 2 == tmp:
                ret += 1
        return ret
# @lc code=end

print(Solution().countTriples(10))