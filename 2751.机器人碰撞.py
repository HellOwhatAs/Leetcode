#
# @lc app=leetcode.cn id=2751 lang=python3
#
# [2751] 机器人碰撞
#

# @lc code=start
from typing import List
import heapq
from itertools import pairwise
class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        idxer = sorted(range(n), key=lambda idx: positions[idx])
        collisions = [(positions[j] - positions[i], ii, jj) for (ii, i), (jj, j) in pairwise(enumerate(idxer))]
        heapq.heapify(collisions)
        while collisions:
            _, ii, jj = heapq.heappop(collisions)
            i, j = idxer[ii], idxer[jj]
            if not (directions[i] == 'R' and directions[j] == 'L'): continue
            if healths[i] == healths[j]:
                healths[i] = healths[j] = 0
                while ii >= 0 and healths[idxer[ii]] == 0: ii -= 1
                if ii < 0: continue
                while jj < n and healths[idxer[jj]] == 0: jj += 1
                if jj >= n: continue
                heapq.heappush(collisions, (positions[idxer[jj]] - positions[idxer[ii]], ii, jj))
            elif healths[i] > healths[j]:
                healths[i] -= 1
                healths[j] = 0
                while jj < n and healths[idxer[jj]] == 0: jj += 1
                if jj >= n: continue
                heapq.heappush(collisions, (positions[idxer[jj]] - positions[i], ii, jj))
            else:
                healths[i] = 0
                healths[j] -= 1
                while ii >= 0 and healths[idxer[ii]] == 0: ii -= 1
                if ii < 0: continue
                heapq.heappush(collisions, (positions[j] - positions[idxer[ii]], ii, jj))
        return [i for i in healths if i > 0]

# @lc code=end

print(Solution().survivedRobotsHealths(positions = [5,4,3,2,1], healths = [2,17,9,15,10], directions = "RRRRR"))
print(Solution().survivedRobotsHealths(positions = [3,5,2,6], healths = [10,10,15,12], directions = "RLRL"))
print(Solution().survivedRobotsHealths(positions = [1,2,5,6], healths = [10,10,11,11], directions = "RLRL"))
print(Solution().survivedRobotsHealths([3,47], [46,26], "LR"))
print(Solution().survivedRobotsHealths([11,44,16], [1,20,17], "RLR"))