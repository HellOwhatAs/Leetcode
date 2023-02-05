#
# @lc app=leetcode.cn id=1210 lang=python3
#
# [1210] 穿过迷宫的最少移动次数
#

# @lc code=start
from typing import List, Tuple
class Solution:
    def next_state(self, state: Tuple[Tuple[int, int], bool]):
        (x0, y0), h = state
        if h:
            if y0 + 1 < self.n and self.grid[x0][y0 + 1] == self.grid[x0 + 1][y0 + 1] == 0:
                yield ((x0, y0 + 1), h)
                yield ((x0, y0), not h)
            if x0 + 2 < self.n and self.grid[x0 + 2][y0] == 0:
                yield ((x0 + 1, y0), h)
        else:
            if y0 + 2 < self.n and self.grid[x0][y0 + 2] == 0:
                yield ((x0, y0 + 1), h)
            if x0 + 1 < self.n and self.grid[x0 + 1][y0] == self.grid[x0 + 1][y0 + 1] == 0:
                yield ((x0 + 1, y0), h)
                yield ((x0, y0), not h)

    def minimumMoves(self, grid: List[List[int]]) -> int:
        self.grid, self.n = grid, len(grid)
        states, dis, vis = [((0, 0), False)], 0, {((0, 0), False)}
        while states:
            dis += 1
            new_states = []
            for state in states:
                for new_state in self.next_state(state):
                    if new_state == ((self.n - 1, self.n - 2), False):
                        return dis
                    if new_state in vis: continue
                    vis.add(new_state)
                    new_states.append(new_state)
            states = new_states
        return -1
# @lc code=end

print(Solution().minimumMoves([[0,0,0,0,0,0,0,0,0,1],[0,1,0,0,0,0,0,1,0,1],[1,0,0,1,0,0,1,0,1,0],[0,0,0,1,0,1,0,1,0,0],[0,0,0,0,1,0,0,0,0,1],[0,0,1,0,0,0,0,0,0,0],[1,0,0,1,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0]]))