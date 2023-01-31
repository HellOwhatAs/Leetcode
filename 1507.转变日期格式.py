#
# @lc app=leetcode.cn id=1507 lang=python3
#
# [1507] 转变日期格式
#

# @lc code=start
class Solution:
    _Month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    Month = lambda x: Solution._Month.index(x) + 1
    Day = lambda x:int("".join(i for i in x if i.isdigit()))
    def reformatDate(self, date: str) -> str:
        day, month, year = date.split()
        return f"{year}-{Solution.Month(month):02d}-{Solution.Day(day):02d}"
# @lc code=end

print(Solution().reformatDate("6th Jun 1933"))