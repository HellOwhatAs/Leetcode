#
# @lc app=leetcode.cn id=1032 lang=python3
#
# [1032] 字符流
#

# @lc code=start
from typing import List
class StreamChecker:

    def __init__(self, words: List[str]):
        self.words = words
        self.d = {}
        for word in words:
            self.func(self.d, word)
        self.cand = [self.d]

    @staticmethod
    def func(d: dict, word: str):
        if len(word) == 1:
            if word in d:d[word][True] = None
            else:d[word] = {True: None}
        else:
            if not word[0] in d: d[word[0]] = {}
            StreamChecker.func(d[word[0]], word[1:])

    def query(self, letter: str) -> bool:
        new_cand = [self.d]
        ret = False
        for d in self.cand:
            if not letter in d: continue
            if True in d[letter]: ret = True
            new_cand.append(d[letter])
        self.cand = new_cand
        return ret


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
# @lc code=end
def test(cmds, args, anss = None):
    obj = None
    if anss is None:
        ret = []
        for cmd, arg in zip(cmds, args):
            if cmd == 'StreamChecker': obj = StreamChecker(*arg)
            else: ret.append(obj.query(*arg))
        return ret
    for cmd, arg, ans in zip(cmds, args, anss):
        if cmd == 'StreamChecker': obj = StreamChecker(*arg)
        else: assert(ans == obj.query(*arg))

test(
    cmds = ["StreamChecker","query","query","query","query","query","query","query","query","query","query","query","query"],
    args = [[["cd","f","kl"]],["a"],["b"],["c"],["d"],["e"],["f"],["g"],["h"],["i"],["j"],["k"],["l"]],
    anss = [None, False, False, False, True, False, True, False, False, False, False, False, True]
)
test(
    cmds = ["StreamChecker","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query","query"],
    args = [[["ab","ba","aaab","abab","baa"]],["a"],["a"],["a"],["a"],["a"],["b"],["a"],["b"],["a"],["b"],["b"],["b"],["a"],["b"],["a"],["b"],["b"],["b"],["b"],["a"],["b"],["a"],["b"],["a"],["a"],["a"],["b"],["a"],["a"],["a"]],
    anss = [None,False,False,False,False,False,True,True,True,True,True,False,False,True,True,True,True,False,False,False,True,True,True,True,True,True,False,True,True,True,False]
)