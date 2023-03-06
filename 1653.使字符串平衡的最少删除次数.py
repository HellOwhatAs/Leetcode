#
# @lc app=leetcode.cn id=1653 lang=python3
#
# [1653] 使字符串平衡的最少删除次数
#

# @lc code=start
class Solution:
    def minimumDeletions(self, s: str) -> int:
        leftb, righta, n, ret = 0, s.count('a'), len(s), float('inf')
        for sep in range(n):
            ret = min(ret, leftb + righta)
            if s[sep] == 'a': righta -= 1
            else: leftb += 1
        return min(ret, leftb + righta)
# @lc code=end

print(Solution().minimumDeletions("aababbab"))
print(Solution().minimumDeletions("bbaaaaabb"))