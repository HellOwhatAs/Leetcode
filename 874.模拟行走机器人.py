#
# @lc app=leetcode.cn id=874 lang=python3
#
# [874] 模拟行走机器人
#

# @lc code=start
from typing import List
class Solution:
    @staticmethod
    def turn(direction: str, code: int) -> str:
        if code == -2: return {'^': '<', '<': 'v', 'v': '>', '>': '^'}[direction]
        elif code == -1: return {'^': '>', '>': 'v', 'v': '<', '<': '^'}[direction]
        raise TypeError(code)

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obstacles_set = {tuple(i) for i in obstacles}
        x, y, direction, dx, dy = 0, 0, '^', 0, 1
        ret = 0
        dxy = {
            '^': (0, 1),
            'v': (0, -1),
            '<': (-1, 0),
            '>': (1, 0)
        }
        for cmd in commands:
            if cmd < 0:
                direction = self.turn(direction, cmd)
                dx, dy = dxy[direction]
            else:
                for _ in range(cmd):
                    tmp = x + dx, y + dy
                    if tmp in obstacles_set: break
                    x, y = tmp
            ret = max(ret, x**2 + y**2)
        return ret

# @lc code=end

print(Solution().robotSim(commands = [4,-1,3], obstacles = []))
print(Solution().robotSim(commands = [4,-1,4,-2,4], obstacles = [[2,4]]))