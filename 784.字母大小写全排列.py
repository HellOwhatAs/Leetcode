#
# @lc app=leetcode.cn id=784 lang=python3
#
# [784] 字母大小写全排列
#

# @lc code=start
from typing import List
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        return (ret:=[s],[ret.extend([j[:i]+j[i].swapcase()+j[i+1:] for j in ret]) for i in range(len(s)) if s[i].isalpha()])[0]
# @lc code=end

print(Solution().letterCasePermutation("3Z4"))