#
# @lc app=leetcode.cn id=1700 lang=python3
#
# [1700] 无法吃午餐的学生数量
#

# @lc code=start
from typing import List
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = [0, 0]
        for i in students: count[i] += 1
        sandwiches.reverse()
        while sandwiches:
            if count[sandwiches[-1]] == 0: break
            count[sandwiches[-1]] -= 1
            sandwiches.pop()
        return sum(count)
# @lc code=end

print(Solution().countStudents(students = [1,1,0,0], sandwiches = [0,1,0,1]))
print(Solution().countStudents(students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]))