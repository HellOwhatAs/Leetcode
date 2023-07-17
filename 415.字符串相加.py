#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#

# @lc code=start
from typing import List
class Solution:
    def func(self, n1: List[int], n2: List[int], idx: int, carry: int = 0):
        if carry == 0 and idx >= len(n1) and idx >= len(n2): return
        tmp = (n1[idx] if idx < len(n1) else 0) + (n2[idx] if idx < len(n2) else 0) + carry
        self.ret.append(tmp % 10)
        self.func(n1, n2, idx + 1, tmp // 10)
    def addStrings(self, num1: str, num2: str) -> str:
        n1, n2 = [ord(c) - ord('0') for c in reversed(num1)], [ord(c) - ord('0') for c in reversed(num2)]
        self.ret = []
        self.func(n1, n2, 0)
        return ''.join(map(str, reversed(self.ret)))
# @lc code=end

print(Solution().addStrings(num1 = "11", num2 = "123"))
print(Solution().addStrings(num1 = "456", num2 = "77"))
print(Solution().addStrings(num1 = "0", num2 = "0"))