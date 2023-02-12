#
# @lc app=leetcode.cn id=1138 lang=python3
#
# [1138] 字母板上的路径
#

# @lc code=start
from itertools import pairwise
from typing import Tuple
class Solution:
    board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
    def get_pos(self, x: str) -> Tuple[int, int]:
        for ii, i in enumerate(self.board):
            if (y:=i.find(x)) != -1: return ii, y
    def get_path(self, start: str, end: str) -> str:
        (sx, sy), (ex, ey) = self.get_pos(start), self.get_pos(end)
        ud, lr = ("U" * (sx - ex) if sx > ex else "D" * (ex - sx)), ("L" * (sy - ey) if sy > ey else "R" * (ey - sy))
        if start == 'z': return ud + lr
        return lr + ud
    def alphabetBoardPath(self, target: str) -> str:
        return self.get_path('a', target[0]) + '!' + "!".join(self.get_path(s, e) for s, e in pairwise(target)) + ('!' if len(target) > 1 else '')
# @lc code=end

print(Solution().alphabetBoardPath("zdz"))