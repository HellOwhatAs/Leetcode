#
# @lc app=leetcode.cn id=735 lang=python3
#
# [735] 行星碰撞
#

# @lc code=start
from typing import List
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for i in asteroids:
            if not s: s.append(i)
            else:
                if not (s[-1] > 0 and i < 0):
                    s.append(i)
                    continue
                if s[-1] > -i: continue
                elif s[-1] < -i:
                    s.pop()
                    # goto line13
                    s.append(i)
                else: s.pop()
        return s
# @lc code=end

print(Solution().asteroidCollision(asteroids = [5,10,-5]))
print(Solution().asteroidCollision(asteroids = [8,-8]))