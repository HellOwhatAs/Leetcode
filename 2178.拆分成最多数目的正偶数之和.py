#
# @lc app=leetcode.cn id=2178 lang=python3
#
# [2178] 拆分成最多数目的正偶数之和
#

# @lc code=start
from typing import List
class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum & 1: return []
        ret = [2]
        finalSum -= 2
        while finalSum >= ret[-1] + 2:
            finalSum -= (ret[-1] + 2)
            ret.append(ret[-1] + 2)
        ret[-1] += finalSum
        return ret

# @lc code=end

print(Solution().maximumEvenSplit(12))
print(Solution().maximumEvenSplit(7))
print(Solution().maximumEvenSplit(28))