#
# @lc app=leetcode.cn id=2437 lang=python3
#
# [2437] 有效时间的数目
#

# @lc code=start
class Solution:
    def countTime(self, time: str) -> int:
        a, b, _, c, d = time
        return (24 if a == b == '?' else ((3 if b in '0123' else 2) if a == '?' else ((4 if a == '2' else 10) if b == '?' else 1))) * (60 if c == d == '?' else (6 if c == '?' else (10 if d == '?' else 1)))
# @lc code=end

print(Solution().countTime(time = "?5:00"))
print(Solution().countTime(time = "0?:0?"))
print(Solution().countTime(time = "??:??"))