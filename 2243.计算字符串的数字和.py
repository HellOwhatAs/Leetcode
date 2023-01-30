#
# @lc app=leetcode.cn id=2243 lang=python3
#
# [2243] 计算字符串的数字和
#

# @lc code=start
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            s = "".join(str(sum(map(int, s[i * k: (i + 1) * k]))) for i in range(len(s) // k + 1) if i * k < len(s))
        return s
# @lc code=end

print(Solution().digitSum("1234", 2))