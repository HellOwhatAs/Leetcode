#
# @lc app=leetcode.cn id=736 lang=python3
#
# [736] Lisp 语法解析
#

# @lc code=start
import json
class Solution:
    def eval(self, x):
        if isinstance(x, list):
            if x[0] == 'let':
                backup, to_delete = {}, []
                for i in range(2, len(x), 2):
                    if x[i-1] in self.gbl: backup[x[i-1]] = self.gbl[x[i-1]]
                    else: to_delete.append(x[i-1])
                    self.gbl[x[i-1]] = self.eval(x[i])
                ret = self.eval(x[-1])
                for k, v in backup.items(): self.gbl[k] = v
                for k in to_delete: self.gbl.pop(k)
                return ret
            elif x[0] == 'add':
                return self.eval(x[1]) + self.eval(x[2])
            elif x[0] == 'mult':
                return self.eval(x[1]) * self.eval(x[2])
            else: raise x
        else:
            if x in self.gbl: return self.gbl[x]
            return int(x)
    def evaluate(self, expression: str) -> int:
        self.gbl = {}
        tree = json.loads(
            expression
            .replace(" (", '",(')
            .replace("(", '("')
            .replace(")", '")')
            .replace(' ', '","')
            .replace(')"', ')')
            .replace('(', '[')
            .replace(')', ']')
        )
        return self.eval(tree)
        
# @lc code=end

print(Solution().evaluate(expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))"))
print(Solution().evaluate(expression = "(let x 3 x 2 x)"))
print(Solution().evaluate(expression = "(let x 1 y 2 x (add x y) (add x y))"))