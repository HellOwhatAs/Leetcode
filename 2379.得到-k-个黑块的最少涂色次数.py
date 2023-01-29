#
# @lc app=leetcode.cn id=2379 lang=python3
#
# [2379] 得到 K 个黑块的最少涂色次数
#

# @lc code=start
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = k - blocks.count('B', 0, k)
        ret = count
        for i in range(k, len(blocks)):
            count -= (blocks[i] == 'B') - (blocks[i - k] == 'B')
            ret = min(ret, count)
        return ret
# @lc code=end

print(Solution().minimumRecolors(blocks = "WBBWWBBWBW", k = 7))