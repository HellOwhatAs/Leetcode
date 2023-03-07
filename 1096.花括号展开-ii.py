#
# @lc app=leetcode.cn id=1096 lang=python3
#
# [1096] 花括号展开 II
#

# @lc code=start
from typing import List, Set
from itertools import product
class Solution:
    def func(self, _start: int, _end: int) -> Set[str]:
        stack = 0
        splits, ret, ssplits = [], [], []
        for i in range(_start, _end):
            if self.expression[i] == '{': stack += 1
            elif self.expression[i] == '}': stack -= 1
            if stack == 0 and self.expression[i] == ',': splits.append(i)
        if splits:
            ssplits.append([_start, splits[0]])
            for i in range(len(splits) - 1):
                ssplits.append([splits[i] + 1, splits[i + 1]])
            ssplits.append([splits[-1] + 1, _end])
        else:
            ssplits = [[_start, _end]]
        for _start, _end in ssplits:

            if self.expression[_start] == '{':
                stack = 1
                for i in range(_start + 1, _end):
                    if self.expression[i] == '{': stack += 1
                    elif self.expression[i] == '}': stack -= 1
                    if stack == 0: break
                if i + 1 == _end:
                    ret.append(self.func(_start + 1, i))
                    continue
                ret.append({a + b for a, b in product(self.func(_start + 1, i), self.func(i + 1, _end))})
            else:
                if _start + 1 == _end: 
                    ret.append({self.expression[_start]})
                    continue
                ret.append({self.expression[_start] + j for j in self.func(_start + 1, _end)})
        
        rret = set()
        for i in ret:
            rret = rret.union(i)
        return rret
    def braceExpansionII(self, expression: str) -> List[str]:
        self.expression  = expression
        return sorted(self.func(0, len(self.expression)))
# @lc code=end
print(Solution().braceExpansionII(expression = "{a,b}{c,{d,e}}"))
print(Solution().braceExpansionII(expression = "{{a,z},a{b,c},{ab,z}}"))
print(Solution().braceExpansionII(expression = '{abc,d}'))