#
# @lc app=leetcode.cn id=2269 lang=python3
#
# [2269] 找到一个数字的 K 美丽值
#

# @lc code=start
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        return (strnum:=str(num), sum((tmp := int(strnum[i - k: i])) != 0 and num % tmp == 0 for i in range(k, len(strnum) + 1)))[1]
# @lc code=end

print(Solution().divisorSubstrings(430043, k = 2))