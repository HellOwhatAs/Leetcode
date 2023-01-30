#
# @lc app=leetcode.cn id=2259 lang=python3
#
# [2259] 移除指定数字得到的最大结果
#

# @lc code=start
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        start = 0
        while start < len(number) and (_tmp:=number.find(digit, start)) != -1:
            tmp = _tmp
            while tmp + 1 < len(number) and number[tmp + 1] == digit: tmp += 1
            if tmp == len(number) - 1: return number[:-1]
            if number[tmp + 1] > digit: return number[:tmp] + number[tmp + 1:]
            start = tmp + 1
        return number[:tmp] + number[tmp + 1:]
# @lc code=end

print(Solution().removeDigit(number = "123", digit = "3"))