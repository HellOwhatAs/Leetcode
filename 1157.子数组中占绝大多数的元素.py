#
# @lc app=leetcode.cn id=1157 lang=python3
#
# [1157] 子数组中占绝大多数的元素
#

# @lc code=start
from typing import List
from collections import defaultdict
import random
from bisect import bisect_left, bisect_right
class MajorityChecker:

    def __init__(self, arr: List[int]):
        self.arr, self.dct = arr, defaultdict(list)
        for i, x in enumerate(arr):
            self.dct[x].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        for _ in range(30):
            x = self.arr[random.randint(left, right)]
            if bisect_right(self.dct[x], right) - bisect_left(self.dct[x], left) >= threshold: return x
        return -1



# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
# @lc code=end
obj = None
for cmd, val in zip(["MajorityChecker", "query", "query", "query"], [[[1, 1, 2, 2, 1, 1]], [0, 5, 4], [0, 3, 3], [2, 3, 2]]):
    if cmd == "MajorityChecker":
        obj = MajorityChecker(*val)
    else:
        print(obj.query(*val))