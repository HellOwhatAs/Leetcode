#
# @lc app=leetcode.cn id=68 lang=python3
#
# [68] 文本左右对齐
#

# @lc code=start
from typing import List
class Solution:
    def valid(self,line:List[str],word:str)->bool:
        return sum([len(i) for i in line])+len(line)+len(word)<=self.maxWidth
    def fillspace(self,line:List[str])->str:
        if len(line)==1:return line[0]+" "*(self.maxWidth-len(line[0]))
        total_spaces=self.maxWidth-sum([len(i) for i in line])
        places=len(line)-1
        base=total_spaces//places
        extra=total_spaces%places
        ret=[]
        for i in range(places):
            ret.append(line[i])
            ret.append(" "*(base+(i<extra)))
        ret.append(line[-1])
        return "".join(ret)
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        paper=[[]]
        self.maxWidth=maxWidth
        for s in words:
            if self.valid(paper[-1],s):
                paper[-1].append(s)
            else:
                paper.append([s])
        for i in range(len(paper)-1):
            paper[i]=self.fillspace(paper[i])
        paper[-1]=" ".join(paper[-1])
        paper[-1]+=" "*(maxWidth-len(paper[-1]))
        return paper
# @lc code=end

print(Solution().fullJustify(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"],20))