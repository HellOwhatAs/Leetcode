#
# @lc app=leetcode.cn id=831 lang=python3
#
# [831] 隐藏个人信息
#

# @lc code=start
class Solution:
    def maskPII(self, s: str) -> str:
        idx = s.find('@')
        if idx == -1:
            nums = "".join(c for c in s if c.isdigit())
            if len(nums) == 10: return f"***-***-{nums[-4:]}"
            return f"+{'*' * (len(nums) - 10)}-***-***-{nums[-4:]}"
        return s[0].lower() + '*' * 5 + s[idx - 1:].lower()
# @lc code=end

print(Solution().maskPII(s = "LeetCode@LeetCode.com"))
print(Solution().maskPII(s = "AB@qq.com"))
print(Solution().maskPII(s = "1(234)567-890"))
print(Solution().maskPII(s = "86-(10)12345678"))