#
# @lc app=leetcode.cn id=1023 lang=python3
#
# [1023] 驼峰式匹配
#

# @lc code=start
from typing import List
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ret = []
        for q in queries:
            i, j = 0, 0
            while i < len(q) and j < len(pattern):
                if q[i] == pattern[j]:  i, j = i + 1, j + 1
                elif q[i].isupper():    break
                else:                   i += 1
            if any(c.isupper() for c in q[i:]): ret.append(False)
            elif j == len(pattern):             ret.append(True)
            else:                               ret.append(False)
        return ret
# @lc code=end

print(Solution().camelMatch(queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"))
print(Solution().camelMatch(queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"))
print(Solution().camelMatch(queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"))