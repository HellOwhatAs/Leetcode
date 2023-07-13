#
# @lc app=leetcode.cn id=1130 lang=python3
#
# [1130] 叶值的最小代价生成树
#

# @lc code=start
from typing import List, Optional
from math import inf
class Solution:
    class Node:
        def __init__(self, val: int, left: Optional['Solution.Node'] = None, right: Optional['Solution.Node'] = None):
            self.val, self.left, self.right = val, left, right
            if left is not None and right is not None:
                self.max_leaf = max(self.left.max_leaf, self.right.max_leaf)
            else:
                assert self.left is self.right is None
                self.max_leaf = self.val
        def __repr__(self) -> str:
            return f"{type(self).__name__}({self.val}, {self.left}, {self.right})"
        
        def __graphviz(self, ret: List[str]) -> None:
            ret.append(f'{id(self)} [label={self.val}];')
            if self.left is self.right is None: return
            ret.append(f'{id(self)} -> {id(self.left)};')
            ret.append(f'{id(self)} -> {id(self.right)};')
            self.left.__graphviz(ret)
            self.right.__graphviz(ret)
            return ret

        def graphviz(self) -> str:
            return '\n'.join(('digraph{', *self.__graphviz([]), '}'))
                    
        def sum_not_leaf(self):
            if self.left is self.right is None: return 0
            return self.val + self.left.sum_not_leaf() + self.right.sum_not_leaf()
    def mctFromLeafValues(self, arr: List[int]) -> int:
        a = [self.Node(i) for i in arr]
        while len(a) > 1:
            min_idx, min_val = None, inf
            for i in range(1, len(a)):
                tmp = a[i-1].max_leaf * a[i].max_leaf
                if min_val > tmp:
                    min_val = tmp
                    min_idx = i-1
            right = a.pop(min_idx + 1)
            a[min_idx] = self.Node(min_val, a[min_idx], right)
        print(a[0].graphviz())
        return a[0].sum_not_leaf()
# @lc code=end

print(Solution().mctFromLeafValues(arr = [6,2,4]))
print(Solution().mctFromLeafValues(arr = [4,11]))