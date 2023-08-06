#
# @lc app=leetcode.cn id=630 lang=python3
#
# [630] 课程表 III
#

# @lc code=start
from typing import List
import heapq

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        selected, now = [], 0
        for duration, lastDay in courses:
            if now + duration <= lastDay:
                heapq.heappush(selected, -duration)
                now += duration
            else:
                if selected and -selected[0] > duration and now + duration + selected[0] <= lastDay:
                    now += heapq.heappop(selected)
                    heapq.heappush(selected, -duration)
                    now += duration
        print(selected)
        return len(selected)
# @lc code=end

print(Solution().scheduleCourse(courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]))
print(Solution().scheduleCourse(courses = [[3,2],[4,3]]))
print(Solution().scheduleCourse([[5,5],[4,6],[2,6]]))
print(Solution().scheduleCourse([[5,15], [3,19], [6,7], [2,10], [5,16], [8,14], [10,11], [2,19]]))