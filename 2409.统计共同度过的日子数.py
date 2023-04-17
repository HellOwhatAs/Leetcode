#
# @lc app=leetcode.cn id=2409 lang=python3
#
# [2409] 统计共同度过的日子数
#

# @lc code=start
import datetime
class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        aa = datetime.datetime(2023, int(arriveAlice[:2]), int(arriveAlice[3:]))
        la = datetime.datetime(2023, int(leaveAlice[:2]), int(leaveAlice[3:]))
        ab = datetime.datetime(2023, int(arriveBob[:2]), int(arriveBob[3:]))
        lb = datetime.datetime(2023, int(leaveBob[:2]), int(leaveBob[3:]))
        return max(0, (min(la, lb) - max(aa, ab)).days + 1)

# @lc code=end

print(Solution().countDaysTogether(arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"))
print(Solution().countDaysTogether(arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"))