#
# @lc app=leetcode.cn id=2569 lang=python3
#
# [2569] 更新数组后处理求和查询
#

# @lc code=start
from typing import List

class Solution:
    def handleQuery(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        n1, val, ret = 0, sum(nums2), []
        for i in reversed(nums1): n1 = (n1 << 1) | i
        for t, l, r in queries:
            if t == 1: n1 ^= ((1 << (r + 1 - l)) - 1) << l
            elif t == 2: val += n1.bit_count() * l
            else: ret.append(val)
        return ret

# @lc code=end
print(Solution().handleQuery(nums1 = [1,0,1], nums2 = [0,0,0], queries = [[1,1,1],[2,1,0],[3,0,0]]))
print(Solution().handleQuery(nums1 = [1], nums2 = [5], queries = [[2,0,0],[3,0,0]]))
print(Solution().handleQuery(
    [0,0,0,0,1,0,0,0,1,1,0,1,0,1,1,1,0,0,0,0,1,1,1],
    [30,46,43,34,39,16,14,41,22,11,32,2,44,12,22,36,44,49,50,10,33,7,42],
    [[1,15,21],[3,0,0],[3,0,0],[2,21,0],[2,13,0],[3,0,0]]
))