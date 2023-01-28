#
# @lc app=leetcode.cn id=2138 lang=python3
#
# [2138] 将字符串拆分为若干长度为 k 的组
#

# @lc code=start
from typing import List
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        return [s[i:i+k] + fill * (i+k-len(s)) if (i+k-len(s)) > 0 else s[i:i+k] for i in range(0, len(s), k)]
# @lc code=end

print(Solution().divideString(s = "abcdefghij", k = 3, fill = "x"))