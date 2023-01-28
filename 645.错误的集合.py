#
# @lc app=leetcode.cn id=645 lang=python3
#
# [645] 错误的集合
#

# @lc code=start
from typing import List
from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ret = [None]*2
        c = Counter(nums)
        for i in range(1, len(c)+2):
            if i in c and c[i]==2: ret[0]=i
            if not i in c: ret[1]=i
            if ret[0]!=None and ret[1]!=None:
                return ret
        return ret
# @lc code=end

print(Solution().findErrorNums([1,1]))