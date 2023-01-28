#
# @lc app=leetcode.cn id=779 lang=python3
#
# [779] 第K个语法符号
#

# @lc code=start
class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n==1:return 0
        if self.kthGrammar(n-1,(k-1)//2+1):return k%2
        else:return int(not k%2)
# @lc code=end

for n in range(1,10):
    for k in range(1,2**(n-1)+1):
        print(Solution().kthGrammar(n,k),end='')
    print()