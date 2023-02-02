#
# @lc app=leetcode.cn id=868 lang=python3
#
# [868] 二进制间距
#

# @lc code=start
class Solution:
    def binaryGap(self, n: int) -> int:
        idx, idxs, ret = 0, -1, 0
        while n:
            if n & 1:
                if idxs != -1: 
                    ret = max(ret, idx - idxs)
                idxs = idx
            idx += 1
            n >>= 1
        return ret
# @lc code=end

print(Solution().binaryGap(5))