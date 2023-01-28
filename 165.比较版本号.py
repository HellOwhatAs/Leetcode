#
# @lc app=leetcode.cn id=165 lang=python3
#
# [165] 比较版本号
#

# @lc code=start
from typing import List
class Solution:
    @staticmethod
    def str2list(x:str)->List[int]:
        return [int(i) for i in x.split('.')]
    def compareVersion(self, version1: str, version2: str) -> int:
        v1,v2=Solution.str2list(version1),Solution.str2list(version2)
        if len(v1)<len(v2):v1.extend([0]*(len(v2)-len(v1)))
        if len(v2)<len(v1):v2.extend([0]*(len(v1)-len(v2)))
        if v1>v2:return 1
        if v1<v2:return -1
        return 0
# @lc code=end

print(Solution().compareVersion(version1 = "0.1", version2 = "1.1"))