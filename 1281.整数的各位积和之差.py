#
# @lc app=leetcode.cn id=1281 lang=python3
#
# [1281] 整数的各位积和之差
#

# @lc code=start
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        Prod, Sum = 1, 0
        while n:
            val = n % 10
            n //= 10
            Prod *= val
            Sum += val
        return Prod - Sum

# @lc code=end

print(Solution().subtractProductAndSum(234))
print(Solution().subtractProductAndSum(4421))