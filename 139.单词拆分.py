#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] 单词拆分
#

# @lc code=start
from typing import List, Dict, Optional, Iterable
from functools import lru_cache

class Solution:

    class Node:
        def __init__(self, init: Optional[Iterable[str]] = None):
            self.next: Dict[str, Solution.Node] = {}
            self.is_leaf: bool = False
            if init is not None:
                for word in init: self.insert(word)

        def insert(self, word: str, start: int = 0):
            if start == len(word):
                self.is_leaf = True
                return
            if not word[start] in self.next: 
                self.next[word[start]] = Solution.Node()
            self.next[word[start]].insert(word, start + 1)
        
        def search(self, pre: str, start: int = 0) -> Optional['Solution.Node']:
            if start == len(pre): return self
            if pre[start] in self.next: return self.next[pre[start]].search(pre, start + 1)
            return None
        
        def extract(self):
            ret: List[str] = []
            self.__dfs(ret, [])
            return ret
        
        def __dfs(self, output: List[str], pre: List[str]):
            if self.is_leaf: output.append(''.join(pre))
            for i in self.next:
                pre.append(i)
                self.next[i].__dfs(output, pre)
                pre.pop()

    @lru_cache(None)
    def dfs(self, start: int):
        if start == len(self.s): return True
        node = self.wordDict
        for i in range(start, len(self.s)):
            node = node.search(self.s[i])
            if node is None: break
            if node.is_leaf:
                if self.dfs(i + 1): return True
        return False


    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.s = s
        self.wordDict = self.Node(wordDict)
        return self.dfs(0)

        

# @lc code=end

# print(Solution().wordBreak(s = "leetleetcode", wordDict = ["leet", "code", "leetcode"]))
# print(Solution().wordBreak(s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]))
# print(Solution().wordBreak(s = "applepenapple", wordDict = ["apple", "pen"]))

print(Solution().wordBreak(
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
    ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))