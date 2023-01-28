#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
from typing import List,Dict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        chr2prime={'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13, 'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43, 'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79, 'w': 83, 'x': 89, 'y': 97, 'z': 101}
        d:Dict[int,List[str]]={}
        for i in strs:
            key=1
            for j in i:
                key*=chr2prime[j]
            if key in d:
                d[key].append(i)
            else:
                d[key]=[i]
        return list(d.values())
            
# @lc code=end