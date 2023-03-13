#
# @lc app=leetcode.cn id=2383 lang=python3
#
# [2383] 赢得比赛需要的最少训练时长
#

# @lc code=start
from typing import List
class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        energy_train = max(0, sum(energy) + 1 - initialEnergy)
        experience_train = 0
        for i in experience:
            if initialExperience > i:
                initialExperience += i
            else:
                experience_train += i - initialExperience + 1
                initialExperience = i * 2 + 1
        return experience_train + energy_train
# @lc code=end

print(Solution().minNumberOfHours(initialEnergy = 5, initialExperience = 3, energy = [1,4,3,2], experience = [2,6,3,1]))
print(Solution().minNumberOfHours(initialEnergy = 2, initialExperience = 4, energy = [1], experience = [3]))