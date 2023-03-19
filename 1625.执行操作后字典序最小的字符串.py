#
# @lc app=leetcode.cn id=1625 lang=python3
#
# [1625] 执行操作后字典序最小的字符串
#

# @lc code=start
from collections import deque
class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        q, vis, ans = deque([s]), {s}, s
        while q:
            s = q.popleft()
            if ans > s: ans = s
            for t in (''.join([str((int(c) + a) % 10) if i & 1 else c for i, c in enumerate(s)]), s[-b:] + s[:-b]):
                if t not in vis: vis.add(t), q.append(t)
        return ans
# @lc code=end

print(Solution().findLexSmallestString(s = "5525", a = 9, b = 2))