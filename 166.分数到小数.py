#
# @lc app=leetcode.cn id=166 lang=python3
#
# [166] 分数到小数
#

# @lc code=start
from typing import List, Optional
class Solution:
    @staticmethod
    def format(nums: List[str], idx: Optional[int] = None, pre: str = ''):
        if len(nums) == 1: return (pre if nums[0] != '0' else '') + nums[0]
        if idx is not None: nums.insert(idx, '('), nums.append(')')
        return f'{pre}{nums[0]}.{"".join(nums[1:])}'
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        pre = '-' if (numerator < 0) != (denominator < 0) else ''
        numerator, denominator = abs(numerator), abs(denominator)
        ret, idxer = [numerator // denominator], {}
        numerator = (numerator % denominator) * 10
        while numerator:
            idxer[numerator] = len(ret)
            ret.append(numerator // denominator)
            numerator = (numerator % denominator) * 10
            if numerator in idxer: break
        else: return self.format([str(i) for i in ret], pre = pre)
        return self.format([str(i) for i in ret], idxer[numerator], pre = pre)
# @lc code=end

print(Solution().fractionToDecimal(numerator = 1, denominator = 2))
print(Solution().fractionToDecimal(numerator = 2, denominator = 1))
print(Solution().fractionToDecimal(numerator = 1145, denominator = 1919))
print(Solution().fractionToDecimal(0, 3))
print(Solution().fractionToDecimal(-50, 8))
print(Solution().fractionToDecimal(-22, -2))
print(Solution().fractionToDecimal(420, 226))
print(Solution().fractionToDecimal(0, -5))