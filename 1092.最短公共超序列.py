#
# @lc app=leetcode.cn id=1092 lang=python3
#
# [1092] 最短公共超序列
#

# @lc code=start
class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        # 初始化一个二维数组，用来存储动态规划的结果
        dp = [[0 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
        # 遍历两个字符串，更新二维数组
        for i in range(1, len(str1) + 1):
            for j in range(1, len(str2) + 1):
                # 如果当前字符相同，那么最长公共子序列长度加一
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                # 否则，取上方或左方的较大值
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        # 初始化一个空字符串，用来存储最短公共超序列
        res = ""
        # 初始化两个指针，分别指向两个字符串的末尾
        i = len(str1)
        j = len(str2)
        # 反向遍历二维数组，直到达到边界
        while i > 0 and j > 0:
            # 如果当前字符相同，那么将其加入最短公共超序列，并将两个指针都向前移动一位
            if str1[i - 1] == str2[j - 1]:
                res = str1[i - 1] + res
                i -= 1
                j -= 1
            # 否则，比较上方和左方的值，取较大者所在的方向，并将对应的字符加入最短公共超序列，同时移动相应的指针
            else:
                if dp[i - 1][j] > dp[i][j - 1]:
                    res = str1[i - 1] + res
                    i -= 1
                else:
                    res = str2[j - 1] + res
                    j -= 1
        # 如果有一个字符串还没有遍历完，那么将其剩余的部分加入最短公共超序列
        if i > 0:
            res = str1[:i] + res
        if j > 0:
            res = str2[:j] + res
        # 返回最短公共超序列
        return res
# @lc code=end

print(Solution().shortestCommonSupersequence(str1 = "abac", str2 = "cab"))