#
# @lc app=leetcode.cn id=481 lang=python3
#
# [481] 神奇字符串
#

# @lc code=start
class Solution:
    @staticmethod
    def func(n:int):
        ret=['1']
        scanner,counter=0,0
        while len(ret)<n:
            if counter==0:
                ret.append('1' if ret[-1]=='2' else '2')
                scanner+=1
                counter=0 if ret[scanner]=='1' else 1
            else:
                ret.append(ret[-1])
                counter-=1
        return "".join(ret)
    def magicalString(self, n: int) -> int:
        return Solution.func(n).count('1')
# @lc code=end

print(Solution().magicalString(6))