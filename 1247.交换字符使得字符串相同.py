#
# @lc app=leetcode.cn id=1247 lang=python3
#
# [1247] 交换字符使得字符串相同
#

# @lc code=start
import numpy as np
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy, yx = np.sum([(int(a == 'x' and b == 'y'), int(a == 'y' and b == 'x')) for a, b in zip(s1, s2)], axis = 0)
        if (xy + yx) % 2 == 1: return -1
        return int(xy // 2 + yx // 2 + xy % 2 + yx % 2)
# @lc code=end

print(Solution().minimumSwap(s1 = "xx", s2 = "yy"))
print(Solution().minimumSwap(s1 = "xxyyxyxyxx", s2 = "xyyxyxxxyx"))