#
# @lc app=leetcode.cn id=859 lang=python3
#
# [859] 亲密字符串
#

# @lc code=start
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal): return False
        diff = [(a, b) for a, b in zip(s, goal) if a != b]
        n = len(diff)
        if n > 2 or n == 1: return False
        if n == 2: return diff[0][0] == diff[1][1] and diff[0][1] == diff[1][0]
        return len(set(s)) < len(s)


# @lc code=end

print(Solution().buddyStrings(s = "abcde", goal = "baced"))