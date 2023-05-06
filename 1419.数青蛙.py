#
# @lc app=leetcode.cn id=1419 lang=python3
#
# [1419] 数青蛙
#

# @lc code=start
class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        waiting, ret = [0, 0, 0, 0, 0], 0
        for c in croakOfFrogs:
            i = 'croak'.index(c)
            if i != 0: waiting[i] -= 1
            if i != 4: waiting[i + 1] += 1
            if min(waiting) < 0: return -1
            ret = max(ret, sum(waiting))
        return ret if all(i == 0 for i in waiting) else -1
            
# @lc code=end

print(Solution().minNumberOfFrogs(croakOfFrogs = "croakcroak"))
print(Solution().minNumberOfFrogs(croakOfFrogs = "crcoakroak"))
print(Solution().minNumberOfFrogs(croakOfFrogs = "croakcrook"))
print(Solution().minNumberOfFrogs(croakOfFrogs = "croakcroa"))