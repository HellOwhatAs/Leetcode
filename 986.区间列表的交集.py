#
# @lc app=leetcode.cn id=986 lang=python3
#
# [986] 区间列表的交集
#

# @lc code=start
from typing import List
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        fs, ss = 0, 0
        ret = []
        a_state, b_state = False, False
        while fs < len(firstList) and ss < len(secondList):
            if a_state and b_state:
                t = min(firstList[fs][1], secondList[ss][1])
            elif a_state and not b_state:
                t = min(firstList[fs][1], secondList[ss][0])
            elif not a_state and b_state:
                t = min(firstList[fs][0], secondList[ss][1])
            else:
                t = min(firstList[fs][0], secondList[ss][0])
            ##################################################
            old_a_state, old_b_state = a_state, b_state
            if fs < len(firstList) and t == firstList[fs][0]:
                a_state = True
            if ss < len(secondList) and t == secondList[ss][0]:
                b_state = True
            if fs < len(firstList) and t == firstList[fs][1]:
                a_state = False
                fs += 1
            if ss < len(secondList) and t == secondList[ss][1]:
                b_state = False
                ss += 1
            ##################################################
            if not (old_a_state and old_b_state) and a_state and b_state:
                ret.append([t])
            if old_a_state ^ a_state and old_b_state ^ b_state and a_state ^ b_state:
                ret.append([t, t])
            if old_a_state and old_b_state and not (a_state and b_state):
                ret[-1].append(t)
            ##################################################
        return ret
# @lc code=end

print(Solution().intervalIntersection(firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]))
print(Solution().intervalIntersection(firstList = [[1,3],[5,9]], secondList = []))
print(Solution().intervalIntersection(firstList = [], secondList = [[4,8],[10,12]]))
print(Solution().intervalIntersection(firstList = [[1,7]], secondList = [[3,10]]))