#
# @lc app=leetcode.cn id=1234 lang=python3
#
# [1234] 替换子串得到平衡字符串
#

# @lc code=start
class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        p, ret = n // 4, n
        Q, W, E, R = [max(0, s.count(c) - p) for c in "QWER"]
        q, w, e, r = 0, 0, 0, 0
        i, j = 0, 0
        while i < n and j <= n:
            while i < n and j < n and (q < Q or w < W or e < E or r < R):
                if s[j] == 'Q': q += 1
                elif s[j] == 'W': w += 1
                elif s[j] == 'E': e += 1
                else: r += 1
                j += 1
            if not (q < Q or w < W or e < E or r < R): ret = min(ret, j - i)
            if s[i] == 'Q': q -= 1
            elif s[i] == 'W': w -= 1
            elif s[i] == 'E': e -= 1
            else: r -= 1
            i += 1
        return ret




# @lc code=end

print(Solution().balancedString("WQWRQQQW"))