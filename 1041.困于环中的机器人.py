#
# @lc app=leetcode.cn id=1041 lang=python3
#
# [1041] 困于环中的机器人
#

# @lc code=start
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, r = 0, 0, 0
        for i in instructions:
            if i == 'L': r = (r - 1) % 4
            elif i == 'R': r = (r + 1) % 4
            else:
                if r == 0: y += 1
                elif r == 1: x += 1
                elif r == 2: y -= 1
                else: x -= 1
        return  x == 0 and y == 0 or r != 0
# @lc code=end

print(Solution().isRobotBounded(instructions = "GGLLGG"))
print(Solution().isRobotBounded(instructions = "GG"))
print(Solution().isRobotBounded(instructions = "GL"))
print(Solution().isRobotBounded("GLRLLGLL"))