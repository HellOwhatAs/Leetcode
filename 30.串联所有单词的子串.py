#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
#

# @lc code=start
from typing import List
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n,k=len(words),len(words[0])
        ret=[]
        word2ind={word:ind for ind,word in enumerate(set(words))}
        unVisited=[0]*len(word2ind)
        for word in words:unVisited[word2ind[word]]+=1
        for i in range(len(s)-k+1):
            if s[i:i+k] in word2ind:
                unvisited=unVisited.copy()
                for j in range(n):
                    tmp=s[i+j*k:i+(j+1)*k]
                    if tmp in word2ind and unvisited[word2ind[tmp]]:
                        unvisited[word2ind[tmp]]-=1
                    else:break
                else:
                    ret.append(i)
        return ret

# @lc code=end

print(Solution().findSubstring("wordgoodgoodgoodbestword",["word","good","best","good"]))