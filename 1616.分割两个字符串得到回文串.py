#
# @lc app=leetcode.cn id=1616 lang=python3
#
# [1616] 分割两个字符串得到回文串
#

# @lc code=start
class Solution:
    @staticmethod
    def left_check(a: str, b: str) -> bool:
        n = len(a)
        for i in range(n):
            if a[i] != b[i]: break
        return i >= n // 2 or a[i:n - i] == a[n - i - 1:i - 1:-1] or b[i:n - i] == b[n - i - 1:i - 1:-1]
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        return self.left_check(a, b[::-1]) or self.left_check(a[::-1], b)
# @lc code=end

print(Solution().checkPalindromeFormation(a = "x", b = "y"))
print(Solution().checkPalindromeFormation(a = "abdef", b = "fecab"))
print(Solution().checkPalindromeFormation(a = "ulacfd", b = "jizalu"))
print(Solution().checkPalindromeFormation("abda", "acmc"))
print(Solution().checkPalindromeFormation("pvhmupgqeltozftlmfjjde", "yjgpzbezspnnpszebzmhvp"))