#
# @lc app=leetcode.cn id=537 lang=python3
#
# [537] 复数乘法
#

# @lc code=start
class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        (r1, c1), (r2, c2) = num1.split('+'), num2.split('+')
        ret = (int(r1) + int(c1[:-1])*1j) * (int(r2) + int(c2[:-1])*1j)
        return "{}+{}i".format(round(ret.real), round(ret.imag))
# @lc code=end

print(Solution().complexNumberMultiply(num1 = "1+1i", num2 = "1+1i"))