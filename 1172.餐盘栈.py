#
# @lc app=leetcode.cn id=1172 lang=python3
#
# [1172] 餐盘栈
#

# @lc code=start
from collections import defaultdict
class DinnerPlates:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = defaultdict(list)
        self.left_not_full = 0
        self.right_not_empty = -1

    def push(self, val: int) -> None:
        if not self.data[self.left_not_full]:
            self.right_not_empty = max(self.right_not_empty, self.left_not_full)
        self.data[self.left_not_full].append(val)
        while len(self.data[self.left_not_full]) == self.capacity:
            self.left_not_full += 1

    def pop(self) -> int:
        if self.right_not_empty == -1: return -1
        if len(self.data[self.right_not_empty]) == self.capacity:
            self.left_not_full = min(self.left_not_full, self.right_not_empty)
        ret = self.data[self.right_not_empty].pop()
        while self.right_not_empty >= 0 and not self.data[self.right_not_empty]:
            self.right_not_empty -= 1
        return ret

    def popAtStack(self, index: int) -> int:
        if not self.data[index]: return -1
        ret = self.data[index].pop()
        self.left_not_full = min(self.left_not_full, index)
        if index == self.right_not_empty:
            while self.right_not_empty >= 0 and not self.data[self.right_not_empty]:
                self.right_not_empty -= 1
        return ret


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
# @lc code=end

