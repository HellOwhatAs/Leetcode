#
# @lc app=leetcode.cn id=1017 lang=python3
#
# [1017] 负二进制转换
#

# @lc code=start
class Solution:
    def baseNeg2(self, n: int) -> str:
        if n < 2: return '01'[n]
        ret = []
        while n:
            ret.append(str(rem := n % 2))
            n -= rem
            n //= -2
        return "".join(reversed(ret))
# @lc code=end

print(Solution().baseNeg2(2))
print(Solution().baseNeg2(3))
print(Solution().baseNeg2(4))