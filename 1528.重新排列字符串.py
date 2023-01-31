#
# @lc app=leetcode.cn id=1528 lang=python3
#
# [1528] 重新排列字符串
#

# @lc code=start
from typing import List
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        return ''.join(s[i] for i in sorted(list(range(len(indices))), key = lambda i: indices[i]))
# @lc code=end

print(Solution().restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3]))