#
# @lc app=leetcode.cn id=2053 lang=python3
#
# [2053] 数组中第 K 个独一无二的字符串
#

# @lc code=start
from typing import List
from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        return ret[k-1] if len(ret:=sorted((k for k,v in Counter(arr).items() if v == 1), key=lambda k:arr.index(k))) > k-1 else ''
# @lc code=end

for i in [
    dict(arr = ["d","b","c","b","c","a"], k = 2),
    dict(arr = ["aaa","aa","a"], k = 1),
    dict(arr = ["a","b","a"], k = 3)  
]:
    print(Solution().kthDistinct(**i))