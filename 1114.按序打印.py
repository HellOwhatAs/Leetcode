#
# @lc app=leetcode.cn id=1114 lang=python3
#
# [1114] 按序打印
#

# @lc code=start
from threading import Lock
class Foo:
    def __init__(self):
        self.l1=Lock()
        self.l2=Lock()
        self.l1.acquire()
        self.l2.acquire()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.l1.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        with self.l1:
            # printSecond() outputs "second". Do not change or remove this line.
            printSecond()
            self.l2.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        with self.l2:
        # printThird() outputs "third". Do not change or remove this line.
            printThird()
# @lc code=end

